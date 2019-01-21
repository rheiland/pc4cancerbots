import ipywidgets as widgets
from hublib.ui import RunCommand, Submit
import xml.etree.ElementTree as ET  # https://docs.python.org/2/library/xml.etree.elementtree.html
import os
import glob
import shutil
import datetime
import tempfile
from config import ConfigTab
from user_params import UserTab
from svg import SVGTab
from substrates import SubstrateTab
from pathlib import Path
from debug import debug_view

# join_our_list = "(Join/ask questions at https://groups.google.com/forum/#!forum/physicell-users)\n"

tab_height = 'auto'
tab_layout = widgets.Layout(width='auto',   # border='2px solid black',
                            height=tab_height, overflow_y='scroll',)

# create the tabs, but don't display yet
config_tab = ConfigTab()

full_filename = os.path.abspath('data/config_cancerbots.xml')
tree = ET.parse(full_filename)  # this file cannot be overwritten; part of tool distro
xml_root = tree.getroot()
user_tab = UserTab()
svg = SVGTab()
sub = SubstrateTab()

nanoHUB_flag = "home/nanohub" in os.environ['HOME']  # True/False (running on nanoHUB or not)


def read_config_cb(_b):
    with debug_view:
        print("read_config_cb", read_config.value)
        # e.g.  "DEFAULT" -> read_config /Users/heiland/dev/pc4cancerbots/data/nanobio_settings.xml
        #       "t360.xml" -> read_config /Users/heiland/.local/share/pc4cancerbots/t360.xml

    if read_config.value is None:  #occurs when a Run just finishes and we update pulldown with the new cache dir??
        with debug_view:
            print("NOTE: read_config_cb(): No read_config.value. Returning!")
        return

    if os.path.isdir(read_config.value):
        is_dir = True
        config_file = os.path.join(read_config.value, 'config.xml')
    else:
        is_dir = False
        config_file = read_config.value

    if Path(config_file).is_file():
        with debug_view:
            print("read_config_cb:  calling fill_gui_params with ",config_file)
        fill_gui_params(config_file)  #should verify file exists!
    else:
        with debug_view:
            print("read_config_cb: ",config_file, " does not exist.")
        return
    
    # update visualization tabs
    if is_dir:
        svg.update(read_config.value)
        sub.update(read_config.value)
    else:  # may want to distinguish "DEFAULT" from other saved .xml config files
        # FIXME: really need a call to clear the visualizations
        svg.update('')
        sub.update('')
        
# Using the param values in the GUI, write a new .xml config file
def write_config_file(name):
    # Read in the default xml config file, just to get a valid 'root' to populate a new one
    full_filename = os.path.abspath('data/config_cancerbots.xml')
    with debug_view:
        print("write_config_file: based on ",full_filename)
    tree = ET.parse(full_filename)  # this file cannot be overwritten; part of tool distro
    xml_root = tree.getroot()
    config_tab.fill_xml(xml_root)
    user_tab.fill_xml(xml_root)
    tree.write(name)


# callback from write_config_button
def write_config_file_cb(b):
    dirname = os.path.expanduser('~/.local/share/pc4cancerbots')
    val = write_config_box.value
    if val == '':
        val = write_config_box.placeholder
    name = os.path.join(dirname, val)
    write_config_file(name)

# Fill the "Load Config" dropdown widget with valid cached results (and 
# default & previous config options)
def get_config_files():
    cf = {'DEFAULT': os.path.abspath('data/config_cancerbots.xml')}
    dirname = os.path.expanduser('~/.local/share/pc4cancerbots')
    try:
        os.makedirs(dirname)
    except:
        pass
    files = glob.glob("%s/*.xml" % dirname)
    # dict.update() will append any new (key,value) pairs
    cf.update(dict(zip(list(map(os.path.basename, files)), files)))

    # Find the dir path (full_path) to the cached dirs
    if nanoHUB_flag:
        full_path = os.path.expanduser("~/data/results/.submit_cache/pc4cancerbots")
    else:
        # local cache
        try:
            cachedir = os.environ['CACHEDIR']
            full_path = os.path.join(cachedir, "pc4cancerbots")
        except:
            print("Exception in get_config_files")
            return cf

    # Put all those cached (full) dirs into a list
    dirs_all = [os.path.join(full_path, f) for f in os.listdir(full_path) if f != '.cache_table']

    # Only want those dirs that contain output files (.svg, .mat, etc), i.e., handle the
    # situation where a user cancels a Run before it really begins, which may create a (mostly) empty cached dir.
    dirs = [f for f in dirs_all if len(os.listdir(f)) > 5]   # "5" somewhat arbitrary
    with debug_view:
        print(dirs)

    # Get a list of sorted dirs, according to creation timestamp (newest -> oldest)
    sorted_dirs = sorted(dirs, key=os.path.getctime, reverse=True)
    with debug_view:
        print(sorted_dirs)
    # Get a list of timestamps associated with each dir
    sorted_dirs_dates = [str(datetime.datetime.fromtimestamp(os.path.getctime(x))) for x in sorted_dirs]
    # Create a dict of {timestamp:dir} pairs
    cached_file_dict = dict(zip(sorted_dirs_dates, sorted_dirs))
    cf.update(cached_file_dict)
    with debug_view:
        print(cf)
    return cf

# Using params in a config (.xml) file, fill GUI widget values in each of the "input" tabs
def fill_gui_params(config_file):
    with debug_view:
        print("fill_gui_params: filling with ",config_file)
    tree = ET.parse(config_file)
    xml_root = tree.getroot()
    config_tab.fill_gui(xml_root)
    user_tab.fill_gui(xml_root)


def run_done_func(s, rdir):
    with debug_view:
        print('run_done_func: results in', rdir)
    
    if nanoHUB_flag:
        # Email the user that their job has completed
        os.system("submit  mail2self -s 'nanoHUB pc4cancerbots' -t 'Your Run completed.'&")

    # save the config file to the cache directory
    shutil.copy('config.xml', rdir)

    # cd out of tmpdir 
    os.chdir(homedir)

    # new results are available, so update dropdown
    # with debug_view:
    #     print('run_done_func: ---- before updating read_config.options')
    read_config.options = get_config_files()
    # with debug_view:
    #     print('run_done_func: ---- after updating read_config.options')

    # and update visualizations
    svg.update(rdir)
    sub.update(rdir)
    with debug_view:
        print('RDF DONE')


# This is used now for the RunCommand
def run_sim_func(s):
    with debug_view:
        print('run_sim_func')

    # make sure we are where we started
    os.chdir(homedir)

    # remove any previous data
    # NOTE: this dir name needs to match the <folder>  in /data/<config_file.xml>
    os.system('rm -rf tmpdir*')
    if os.path.isdir('tmpdir'):
        # something on NFS causing issues...
        tname = tempfile.mkdtemp(suffix='.bak', prefix='tmpdir_', dir='.')
        shutil.move('tmpdir', tname)
    os.makedirs('tmpdir')

    # write the default config file to tmpdir
    new_config_file = "tmpdir/config.xml"
    write_config_file(new_config_file)  

    with open(new_config_file) as f:
        run_name = s.make_rname(f.read())

    tdir = os.path.abspath('tmpdir')
    os.chdir(tdir)  # operate from tmpdir; temporary output goes here.  may be copied to cache later
    svg.update(tdir)
    sub.update(tdir)

    if nanoHUB_flag:
        if remote_cb.value:
            # s.run(run_name, "-n 8 -w 1440 pc4nanobio-r77 config.xml")  # will wait in standby queue forever
            # s.run(run_name, "-w 7200 pc4nanobio-r77 config.xml") 
            s.run(run_name, "-v ncn-hub_M@brown -n 8 -w 1440 pc4cancerbots-r77 config.xml") 
        else:
            # read_config.index = 0   # reset Dropdown 'Load Config' to 'DEFAULT' when Run interactively
            s.run(run_name, "--local ../bin/cancerbots config.xml")
    else:
        # reset Dropdown 'Load Config' to 'DEFAULT' when Run interactively
        # Warning: this will trigger read_config_cb() !!
        # read_config.index = 0   
        s.run("../bin/cancerbots config.xml", runname=run_name)

    with debug_view:
        print('run_sim_func DONE')


def outcb(s):
    # This is called when new output is received.
    # Only update file list for certain messages: 
    if "simulat" in s:
        # New Data. update visualizations
        svg.update('')
        sub.update('')
    return s


if nanoHUB_flag:
    run_button = Submit(label='Run',
                       start_func=run_sim_func,
                        done_func=run_done_func,
                        cachename='pc4cancerbots',
                        showcache=False,
                        outcb=outcb)
else:
    run_button = RunCommand(start_func=run_sim_func,
                            done_func=run_done_func,
                            cachename='pc4cancerbots',
                            showcache=False,
                            outcb=outcb)  

read_config = widgets.Dropdown(
    description='Load Config',
    options=get_config_files(),
    tooltip='Config File or Previous Run',
)
read_config.style = {'description_width': '%sch' % str(len(read_config.description) + 1)}
read_config.observe(read_config_cb, names='value') 

# write_config_button = widgets.Button(
#     description='Write config file',
#     button_style='success',  # 'success', 'info', 'warning', 'danger' or ''
#     tooltip='Generate XML',
# )
# write_config_button.on_click(write_config_file_cb)
# write_config_box = widgets.Text(
#     placeholder='my_nanobio_settings.xml',
#     description='',
# )
# write_config_row = widgets.HBox([write_config_button, write_config_box])

titles = ['Config Basics', 'User Params', 'Cell Plots', 'Substrate Plots']
tabs = widgets.Tab(children=[config_tab.tab, user_tab.tab, svg.tab, sub.tab],
                   _titles={i: t for i, t in enumerate(titles)},
                   layout=tab_layout)

homedir = os.getcwd()

if nanoHUB_flag:
    remote_cb = widgets.Checkbox(indent=False, value=False, description='Submit as Batch Job to Clusters/Grid')
    #gui = widgets.VBox(children=[read_config, tabs, write_config_row, remote_cb, run_button.w])
    gui = widgets.VBox(children=[read_config, tabs, remote_cb, run_button.w])
else:
    #gui = widgets.VBox(children=[read_config, tabs, write_config_row, run_button.w])
    gui = widgets.VBox(children=[read_config, tabs, run_button.w])
fill_gui_params(read_config.options['DEFAULT'])
