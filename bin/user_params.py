 
# This file is auto-generated from a Python script that parses a PhysiCell configuration (.xml) file.
#
# Edit at your own risk.
#
import os
from ipywidgets import Label,Text,Checkbox,Button,HBox,VBox,FloatText,IntText,BoundedIntText,BoundedFloatText
    
class UserTab(object):

    def __init__(self):
        
        micron_units = Label('micron')   # use "option m" (Mac, for micro symbol)

        constWidth = '180px'
        tab_height = '500px'
        stepsize = 10

        style = {'description_width': '250px'}
        layout = {'width': '400px'}

        self.random_seed = IntText(
          description='random_seed',
          value=0,
          step=1,
          style=style, layout=layout)

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

        self.attached_worker_migration_bias = FloatText(
          description='attached_worker_migration_bias',
          value=0.5,
          step=0.1,
          style=style, layout=layout)

        self.unattached_worker_migration_bias = FloatText(
          description='unattached_worker_migration_bias',
          value=0.5,
          step=0.1,
          style=style, layout=layout)

        self.tab = VBox([
          HBox([self.random_seed, Label('')]), 
          HBox([self.therapy_activation_time, Label('min')]), 
          HBox([self.save_interval_after_therapy_start, Label('min')]), 
          HBox([self.cargo_o2_relative_uptake, Label('')]), 
          HBox([self.cargo_apoptosis_rate, Label('1/min')]), 
          HBox([self.cargo_relative_adhesion, Label('')]), 
          HBox([self.cargo_relative_repulsion, Label('')]), 
          HBox([self.worker_o2_relative_uptake, Label('1/min')]), 
          HBox([self.worker_apoptosis_rate, Label('1/min')]), 
          HBox([self.worker_motility_persistence_time, Label('min')]), 
          HBox([self.worker_migration_speed, Label('micron/min')]), 
          HBox([self.worker_relative_adhesion, Label('')]), 
          HBox([self.worker_relative_repulsion, Label('')]), 
          HBox([self.elastic_coefficient, Label('1/min')]), 
          HBox([self.receptor, Label('')]), 
          HBox([self.cargo_release_o2_threshold, Label('mmHg')]), 
          HBox([self.max_relative_cell_adhesion_distance, Label('')]), 
          HBox([self.damage_rate, Label('1/min')]), 
          HBox([self.repair_rate, Label('1/min')]), 
          HBox([self.drug_death_rate, Label('1/min')]), 
          HBox([self.worker_fraction, Label('')]), 
          HBox([self.number_of_injected_cells, Label('')]), 
          HBox([self.tumor_radius, Label('micron')]), 
          HBox([self.max_elastic_displacement, Label('micron')]), 
          HBox([self.attachment_receptor_threshold, Label('')]), 
          HBox([self.max_attachment_distance, Label('micron')]), 
          HBox([self.min_attachment_distance, Label('micron')]), 
          HBox([self.motility_shutdown_detection_threshold, Label('')]), 
          HBox([self.attached_worker_migration_bias, Label('')]), 
          HBox([self.unattached_worker_migration_bias, Label('')]), 
        ])

    # Populate the GUI widgets with values from the XML
    def fill_gui(self, xml_root):
        uep = xml_root.find('.//user_parameters')  # find unique entry point into XML
        self.random_seed.value = int(uep.find('.//random_seed').text)
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
        self.attached_worker_migration_bias.value = float(uep.find('.//attached_worker_migration_bias').text)
        self.unattached_worker_migration_bias.value = float(uep.find('.//unattached_worker_migration_bias').text)


    # Read values from the GUI widgets to enable editing XML
    def fill_xml(self, xml_root):
        uep = xml_root.find('.//user_parameters')  # find unique entry point into XML 
        uep.find('.//random_seed').text = str(self.random_seed.value)
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
        uep.find('.//attached_worker_migration_bias').text = str(self.attached_worker_migration_bias.value)
        uep.find('.//unattached_worker_migration_bias').text = str(self.unattached_worker_migration_bias.value)
