 
# This file is auto-generated from a Python script that parses a PhysiCell configuration (.xml) file.
#
# Edit at your own risk.
#
import os
from ipywidgets import Label,Text,Checkbox,Button,HBox,VBox,FloatText,IntText,BoundedIntText,BoundedFloatText,Layout,Box
    
class UserTab(object):

    def __init__(self):
        
        micron_units = Label('micron')   # use "option m" (Mac, for micro symbol)

        constWidth = '180px'
        tab_height = '500px'
        stepsize = 10

        style = {'description_width': '250px'}
        layout = {'width': '400px'}

        self.therapy_activation_time = FloatText(
          description='therapy_activation_time',
          value=10080,
          step=1000,
          style=style, layout=layout)

        self.save_interval_after_therapy_start = FloatText(
          description='save_interval_after_therapy_start',
          value=3,
          step=0.1,
          style=style, layout=layout)

        self.cargo_o2_relative_uptake = FloatText(
          description='cargo_o2_relative_uptake',
          value=0.1,
          step=0.01,
          style=style, layout=layout)

        self.cargo_apoptosis_rate = FloatText(
          description='cargo_apoptosis_rate',
          value=4.065e-5,
          step=1e-05,
          style=style, layout=layout)

        self.cargo_relative_adhesion = FloatText(
          description='cargo_relative_adhesion',
          value=0,
          step=0.01,
          style=style, layout=layout)

        self.cargo_relative_repulsion = FloatText(
          description='cargo_relative_repulsion',
          value=5,
          step=0.1,
          style=style, layout=layout)

        self.worker_o2_relative_uptake = FloatText(
          description='worker_o2_relative_uptake',
          value=0.1,
          step=0.01,
          style=style, layout=layout)

        self.worker_apoptosis_rate = FloatText(
          description='worker_apoptosis_rate',
          value=0,
          step=0.01,
          style=style, layout=layout)

        self.worker_motility_persistence_time = FloatText(
          description='worker_motility_persistence_time',
          value=5.0,
          step=0.1,
          style=style, layout=layout)

        self.worker_migration_speed = FloatText(
          description='worker_migration_speed',
          value=2.0,
          step=0.1,
          style=style, layout=layout)

        self.attached_worker_migration_bias = FloatText(
          description='attached_worker_migration_bias',
          value=1.0,
          step=0.1,
          style=style, layout=layout)

        self.unattached_worker_migration_bias = FloatText(
          description='unattached_worker_migration_bias',
          value=1.0,
          step=0.1,
          style=style, layout=layout)

        self.worker_relative_adhesion = FloatText(
          description='worker_relative_adhesion',
          value=0,
          step=0.01,
          style=style, layout=layout)

        self.worker_relative_repulsion = FloatText(
          description='worker_relative_repulsion',
          value=5,
          step=0.1,
          style=style, layout=layout)

        self.elastic_coefficient = FloatText(
          description='elastic_coefficient',
          value=0.05,
          step=0.01,
          style=style, layout=layout)

        self.receptor = FloatText(
          description='receptor',
          value=0.0,
          step=0.01,
          style=style, layout=layout)

        self.cargo_release_o2_threshold = FloatText(
          description='cargo_release_o2_threshold',
          value=10,
          step=1,
          style=style, layout=layout)

        self.max_relative_cell_adhesion_distance = FloatText(
          description='max_relative_cell_adhesion_distance',
          value=1.25,
          step=0.1,
          style=style, layout=layout)

        self.damage_rate = FloatText(
          description='damage_rate',
          value=0.03333,
          step=0.01,
          style=style, layout=layout)

        self.repair_rate = FloatText(
          description='repair_rate',
          value=0.004167,
          step=0.001,
          style=style, layout=layout)

        self.drug_death_rate = FloatText(
          description='drug_death_rate',
          value=0.004167,
          step=0.001,
          style=style, layout=layout)

        self.worker_fraction = FloatText(
          description='worker_fraction',
          value=0.10,
          step=0.01,
          style=style, layout=layout)

        self.number_of_injected_cells = IntText(
          description='number_of_injected_cells',
          value=500,
          step=10,
          style=style, layout=layout)

        self.tumor_radius = FloatText(
          description='tumor_radius',
          value=200,
          step=10,
          style=style, layout=layout)

        self.max_elastic_displacement = FloatText(
          description='max_elastic_displacement',
          value=50.0,
          step=1,
          style=style, layout=layout)

        self.attachment_receptor_threshold = FloatText(
          description='attachment_receptor_threshold',
          value=0.1,
          step=0.01,
          style=style, layout=layout)

        self.max_attachment_distance = FloatText(
          description='max_attachment_distance',
          value=18.0,
          step=1,
          style=style, layout=layout)

        self.min_attachment_distance = FloatText(
          description='min_attachment_distance',
          value=14.0,
          step=1,
          style=style, layout=layout)

        self.motility_shutdown_detection_threshold = FloatText(
          description='motility_shutdown_detection_threshold',
          value=0.001,
          step=0.0001,
          style=style, layout=layout)

        param_button_layout={'width':'400px'} 

        desc_row1 = Button(description='time at which therapy begins', disabled=True, layout=param_button_layout) 
        desc_row1.style.button_color = 'lightgreen'
        desc_row2 = Button(description='save (output) interval after therapy begins', disabled=True, layout=param_button_layout) 
        desc_row2.style.button_color = 'tan'
        desc_row3 = Button(description='oxygen uptake for cargo cells', disabled=True, layout=param_button_layout) 
        desc_row3.style.button_color = 'lightgreen'
        desc_row4 = Button(description='apoptosis rate for cargo cells', disabled=True, layout=param_button_layout) 
        desc_row4.style.button_color = 'tan'
        desc_row5 = Button(description='relative adhesion for cargo cells', disabled=True, layout=param_button_layout) 
        desc_row5.style.button_color = 'lightgreen'
        desc_row6 = Button(description='relative repulsion for cargo cells', disabled=True, layout=param_button_layout) 
        desc_row6.style.button_color = 'tan'
        desc_row7 = Button(description='oxygen uptake for worker cells', disabled=True, layout=param_button_layout) 
        desc_row7.style.button_color = 'lightgreen'
        desc_row8 = Button(description='apoptosis rate for workers', disabled=True, layout=param_button_layout) 
        desc_row8.style.button_color = 'tan'
        desc_row9 = Button(description='motility persistence of workers', disabled=True, layout=param_button_layout) 
        desc_row9.style.button_color = 'lightgreen'
        desc_row10 = Button(description='migration speed for workers', disabled=True, layout=param_button_layout) 
        desc_row10.style.button_color = 'tan'
        desc_row11 = Button(description='migration bias for attached workers', disabled=True, layout=param_button_layout) 
        desc_row11.style.button_color = 'lightgreen'
        desc_row12 = Button(description='migration bias for unattached workers', disabled=True, layout=param_button_layout) 
        desc_row12.style.button_color = 'tan'
        desc_row13 = Button(description='relative adhesion for workers', disabled=True, layout=param_button_layout) 
        desc_row13.style.button_color = 'lightgreen'
        desc_row14 = Button(description='relative repulsion for workers', disabled=True, layout=param_button_layout) 
        desc_row14.style.button_color = 'tan'
        desc_row15 = Button(description='elastic coefficient of cells', disabled=True, layout=param_button_layout) 
        desc_row15.style.button_color = 'lightgreen'
        desc_row16 = Button(description='receptor initial value', disabled=True, layout=param_button_layout) 
        desc_row16.style.button_color = 'tan'
        desc_row17 = Button(description='oxygen threshold for releasing cargo', disabled=True, layout=param_button_layout) 
        desc_row17.style.button_color = 'lightgreen'
        desc_row18 = Button(description='max distance cells can adhere', disabled=True, layout=param_button_layout) 
        desc_row18.style.button_color = 'tan'
        desc_row19 = Button(description='damage rate during therapy', disabled=True, layout=param_button_layout) 
        desc_row19.style.button_color = 'lightgreen'
        desc_row20 = Button(description='repair rate during therapy', disabled=True, layout=param_button_layout) 
        desc_row20.style.button_color = 'tan'
        desc_row21 = Button(description='death rate for drug', disabled=True, layout=param_button_layout) 
        desc_row21.style.button_color = 'lightgreen'
        desc_row22 = Button(description='fraction of cells that are workers', disabled=True, layout=param_button_layout) 
        desc_row22.style.button_color = 'tan'
        desc_row23 = Button(description='# of agents for therapy', disabled=True, layout=param_button_layout) 
        desc_row23.style.button_color = 'lightgreen'
        desc_row24 = Button(description='initial tumor radius', disabled=True, layout=param_button_layout) 
        desc_row24.style.button_color = 'tan'
        desc_row25 = Button(description='max elastic displacement for cells', disabled=True, layout=param_button_layout) 
        desc_row25.style.button_color = 'lightgreen'
        desc_row26 = Button(description='threshold for attachment', disabled=True, layout=param_button_layout) 
        desc_row26.style.button_color = 'tan'
        desc_row27 = Button(description='max attachment distance', disabled=True, layout=param_button_layout) 
        desc_row27.style.button_color = 'lightgreen'
        desc_row28 = Button(description='min attachment distance', disabled=True, layout=param_button_layout) 
        desc_row28.style.button_color = 'tan'
        desc_row29 = Button(description='worker stops if chemoattractant < threshold', disabled=True, layout=param_button_layout) 
        desc_row29.style.button_color = 'lightgreen'

        row1 = [self.therapy_activation_time, Label('min' , layout=Layout(flex='1 1 auto', width='auto')), desc_row1] 
        row2 = [self.save_interval_after_therapy_start, Label('min' , layout=Layout(flex='1 1 auto', width='auto')), desc_row2] 
        row3 = [self.cargo_o2_relative_uptake, Label('' , layout=Layout(flex='1 1 auto', width='auto')), desc_row3] 
        row4 = [self.cargo_apoptosis_rate, Label('1/min' , layout=Layout(flex='1 1 auto', width='auto')), desc_row4] 
        row5 = [self.cargo_relative_adhesion, Label('' , layout=Layout(flex='1 1 auto', width='auto')), desc_row5] 
        row6 = [self.cargo_relative_repulsion, Label('' , layout=Layout(flex='1 1 auto', width='auto')), desc_row6] 
        row7 = [self.worker_o2_relative_uptake, Label('1/min' , layout=Layout(flex='1 1 auto', width='auto')), desc_row7] 
        row8 = [self.worker_apoptosis_rate, Label('1/min' , layout=Layout(flex='1 1 auto', width='auto')), desc_row8] 
        row9 = [self.worker_motility_persistence_time, Label('min' , layout=Layout(flex='1 1 auto', width='auto')), desc_row9] 
        row10 = [self.worker_migration_speed, Label('micron/min' , layout=Layout(flex='1 1 auto', width='auto')), desc_row10] 
        row11 = [self.attached_worker_migration_bias, Label('' , layout=Layout(flex='1 1 auto', width='auto')), desc_row11] 
        row12 = [self.unattached_worker_migration_bias, Label('' , layout=Layout(flex='1 1 auto', width='auto')), desc_row12] 
        row13 = [self.worker_relative_adhesion, Label('' , layout=Layout(flex='1 1 auto', width='auto')), desc_row13] 
        row14 = [self.worker_relative_repulsion, Label('' , layout=Layout(flex='1 1 auto', width='auto')), desc_row14] 
        row15 = [self.elastic_coefficient, Label('1/min' , layout=Layout(flex='1 1 auto', width='auto')), desc_row15] 
        row16 = [self.receptor, Label('' , layout=Layout(flex='1 1 auto', width='auto')), desc_row16] 
        row17 = [self.cargo_release_o2_threshold, Label('mmHg' , layout=Layout(flex='1 1 auto', width='auto')), desc_row17] 
        row18 = [self.max_relative_cell_adhesion_distance, Label('' , layout=Layout(flex='1 1 auto', width='auto')), desc_row18] 
        row19 = [self.damage_rate, Label('1/min' , layout=Layout(flex='1 1 auto', width='auto')), desc_row19] 
        row20 = [self.repair_rate, Label('1/min' , layout=Layout(flex='1 1 auto', width='auto')), desc_row20] 
        row21 = [self.drug_death_rate, Label('1/min' , layout=Layout(flex='1 1 auto', width='auto')), desc_row21] 
        row22 = [self.worker_fraction, Label('' , layout=Layout(flex='1 1 auto', width='auto')), desc_row22] 
        row23 = [self.number_of_injected_cells, Label('' , layout=Layout(flex='1 1 auto', width='auto')), desc_row23] 
        row24 = [self.tumor_radius, Label('micron' , layout=Layout(flex='1 1 auto', width='auto')), desc_row24] 
        row25 = [self.max_elastic_displacement, Label('micron' , layout=Layout(flex='1 1 auto', width='auto')), desc_row25] 
        row26 = [self.attachment_receptor_threshold, Label('' , layout=Layout(flex='1 1 auto', width='auto')), desc_row26] 
        row27 = [self.max_attachment_distance, Label('micron' , layout=Layout(flex='1 1 auto', width='auto')), desc_row27] 
        row28 = [self.min_attachment_distance, Label('micron' , layout=Layout(flex='1 1 auto', width='auto')), desc_row28] 
        row29 = [self.motility_shutdown_detection_threshold, Label('' , layout=Layout(flex='1 1 auto', width='auto')), desc_row29] 

        box_layout = Layout(display='flex', flex_flow='row', align_items='stretch', width='100%')
        box1 = Box(children=row1, layout=box_layout)
        box2 = Box(children=row2, layout=box_layout)
        box3 = Box(children=row3, layout=box_layout)
        box4 = Box(children=row4, layout=box_layout)
        box5 = Box(children=row5, layout=box_layout)
        box6 = Box(children=row6, layout=box_layout)
        box7 = Box(children=row7, layout=box_layout)
        box8 = Box(children=row8, layout=box_layout)
        box9 = Box(children=row9, layout=box_layout)
        box10 = Box(children=row10, layout=box_layout)
        box11 = Box(children=row11, layout=box_layout)
        box12 = Box(children=row12, layout=box_layout)
        box13 = Box(children=row13, layout=box_layout)
        box14 = Box(children=row14, layout=box_layout)
        box15 = Box(children=row15, layout=box_layout)
        box16 = Box(children=row16, layout=box_layout)
        box17 = Box(children=row17, layout=box_layout)
        box18 = Box(children=row18, layout=box_layout)
        box19 = Box(children=row19, layout=box_layout)
        box20 = Box(children=row20, layout=box_layout)
        box21 = Box(children=row21, layout=box_layout)
        box22 = Box(children=row22, layout=box_layout)
        box23 = Box(children=row23, layout=box_layout)
        box24 = Box(children=row24, layout=box_layout)
        box25 = Box(children=row25, layout=box_layout)
        box26 = Box(children=row26, layout=box_layout)
        box27 = Box(children=row27, layout=box_layout)
        box28 = Box(children=row28, layout=box_layout)
        box29 = Box(children=row29, layout=box_layout)

        self.tab = VBox([
          box1,
          box2,
          box3,
          box4,
          box5,
          box6,
          box7,
          box8,
          box9,
          box10,
          box11,
          box12,
          box13,
          box14,
          box15,
          box16,
          box17,
          box18,
          box19,
          box20,
          box21,
          box22,
          box23,
          box24,
          box25,
          box26,
          box27,
          box28,
          box29,
        ])

    # Populate the GUI widgets with values from the XML
    def fill_gui(self, xml_root):
        uep = xml_root.find('.//user_parameters')  # find unique entry point into XML
        self.therapy_activation_time.value = float(uep.find('.//therapy_activation_time').text)
        self.save_interval_after_therapy_start.value = float(uep.find('.//save_interval_after_therapy_start').text)
        self.cargo_o2_relative_uptake.value = float(uep.find('.//cargo_o2_relative_uptake').text)
        self.cargo_apoptosis_rate.value = float(uep.find('.//cargo_apoptosis_rate').text)
        self.cargo_relative_adhesion.value = float(uep.find('.//cargo_relative_adhesion').text)
        self.cargo_relative_repulsion.value = float(uep.find('.//cargo_relative_repulsion').text)
        self.worker_o2_relative_uptake.value = float(uep.find('.//worker_o2_relative_uptake').text)
        self.worker_apoptosis_rate.value = float(uep.find('.//worker_apoptosis_rate').text)
        self.worker_motility_persistence_time.value = float(uep.find('.//worker_motility_persistence_time').text)
        self.worker_migration_speed.value = float(uep.find('.//worker_migration_speed').text)
        self.attached_worker_migration_bias.value = float(uep.find('.//attached_worker_migration_bias').text)
        self.unattached_worker_migration_bias.value = float(uep.find('.//unattached_worker_migration_bias').text)
        self.worker_relative_adhesion.value = float(uep.find('.//worker_relative_adhesion').text)
        self.worker_relative_repulsion.value = float(uep.find('.//worker_relative_repulsion').text)
        self.elastic_coefficient.value = float(uep.find('.//elastic_coefficient').text)
        self.receptor.value = float(uep.find('.//receptor').text)
        self.cargo_release_o2_threshold.value = float(uep.find('.//cargo_release_o2_threshold').text)
        self.max_relative_cell_adhesion_distance.value = float(uep.find('.//max_relative_cell_adhesion_distance').text)
        self.damage_rate.value = float(uep.find('.//damage_rate').text)
        self.repair_rate.value = float(uep.find('.//repair_rate').text)
        self.drug_death_rate.value = float(uep.find('.//drug_death_rate').text)
        self.worker_fraction.value = float(uep.find('.//worker_fraction').text)
        self.number_of_injected_cells.value = int(uep.find('.//number_of_injected_cells').text)
        self.tumor_radius.value = float(uep.find('.//tumor_radius').text)
        self.max_elastic_displacement.value = float(uep.find('.//max_elastic_displacement').text)
        self.attachment_receptor_threshold.value = float(uep.find('.//attachment_receptor_threshold').text)
        self.max_attachment_distance.value = float(uep.find('.//max_attachment_distance').text)
        self.min_attachment_distance.value = float(uep.find('.//min_attachment_distance').text)
        self.motility_shutdown_detection_threshold.value = float(uep.find('.//motility_shutdown_detection_threshold').text)


    # Read values from the GUI widgets to enable editing XML
    def fill_xml(self, xml_root):
        uep = xml_root.find('.//user_parameters')  # find unique entry point into XML 
        uep.find('.//therapy_activation_time').text = str(self.therapy_activation_time.value)
        uep.find('.//save_interval_after_therapy_start').text = str(self.save_interval_after_therapy_start.value)
        uep.find('.//cargo_o2_relative_uptake').text = str(self.cargo_o2_relative_uptake.value)
        uep.find('.//cargo_apoptosis_rate').text = str(self.cargo_apoptosis_rate.value)
        uep.find('.//cargo_relative_adhesion').text = str(self.cargo_relative_adhesion.value)
        uep.find('.//cargo_relative_repulsion').text = str(self.cargo_relative_repulsion.value)
        uep.find('.//worker_o2_relative_uptake').text = str(self.worker_o2_relative_uptake.value)
        uep.find('.//worker_apoptosis_rate').text = str(self.worker_apoptosis_rate.value)
        uep.find('.//worker_motility_persistence_time').text = str(self.worker_motility_persistence_time.value)
        uep.find('.//worker_migration_speed').text = str(self.worker_migration_speed.value)
        uep.find('.//attached_worker_migration_bias').text = str(self.attached_worker_migration_bias.value)
        uep.find('.//unattached_worker_migration_bias').text = str(self.unattached_worker_migration_bias.value)
        uep.find('.//worker_relative_adhesion').text = str(self.worker_relative_adhesion.value)
        uep.find('.//worker_relative_repulsion').text = str(self.worker_relative_repulsion.value)
        uep.find('.//elastic_coefficient').text = str(self.elastic_coefficient.value)
        uep.find('.//receptor').text = str(self.receptor.value)
        uep.find('.//cargo_release_o2_threshold').text = str(self.cargo_release_o2_threshold.value)
        uep.find('.//max_relative_cell_adhesion_distance').text = str(self.max_relative_cell_adhesion_distance.value)
        uep.find('.//damage_rate').text = str(self.damage_rate.value)
        uep.find('.//repair_rate').text = str(self.repair_rate.value)
        uep.find('.//drug_death_rate').text = str(self.drug_death_rate.value)
        uep.find('.//worker_fraction').text = str(self.worker_fraction.value)
        uep.find('.//number_of_injected_cells').text = str(self.number_of_injected_cells.value)
        uep.find('.//tumor_radius').text = str(self.tumor_radius.value)
        uep.find('.//max_elastic_displacement').text = str(self.max_elastic_displacement.value)
        uep.find('.//attachment_receptor_threshold').text = str(self.attachment_receptor_threshold.value)
        uep.find('.//max_attachment_distance').text = str(self.max_attachment_distance.value)
        uep.find('.//min_attachment_distance').text = str(self.min_attachment_distance.value)
        uep.find('.//motility_shutdown_detection_threshold').text = str(self.motility_shutdown_detection_threshold.value)
