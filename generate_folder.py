#!/usr/bin/env python

import os
import sys
#import ConfigParser
import subprocess
from shutil import copyfile, copytree
if __name__ == "__main__":

    #switchOn = ['2','4','5','7','9','21','22','24','25','29','30','31','32','33','34']
    #switchOn = ['2', '4', '7', '21', '24', '25', '31', '32', '33', '34'] # production succeeded
    switchOn = [str(i) for i in range(30, 50)]
    #switchOn = ['13']
    params = [( '1' , 'cG'),
            ('2' , 'cW'),
            ('3' , 'cH'),
            ('4' , 'cHbox'),
            ('5' , 'cHDD'),
            ('6' , 'cHG'),
            ('7' , 'cHW'),
            ('8' , 'cHB'),
            ('9' , 'cHWB'),
            ('10' , 'ceHRe'),
            ('11' , 'cuHRe'),
            ('12' , 'cdHRe'),
            ('13' , 'ceWRe'),
            ('14' , 'ceBRe'),
            ('15' , 'cuGRe'),
            ('16' , 'cuWRe'),
            ('17' , 'cuBRe'),
            ('18' , 'cdGRe'),
            ('19' , 'cdWRe'),
            ('20' , 'cdBRe'),
            ('21' , 'cHl1'),
            ('22' , 'cHl3'),
            ('23' , 'cHe'),
            ('24' , 'cHq1'),
            ('25' , 'cHq3'),
            ('26' , 'cHu'),
            ('27' , 'cHd'),
            ('28' , 'cHudRe'),
            ('29' , 'cll'),
            ('30' , 'cll1'),
            ('31' , 'cqq1'),
            ('32' , 'cqq11'),
            ('33' , 'cqq3'),
            ('34' , 'cqq31'),
            ('35' , 'clq1'),
            ('36' , 'clq3'),
            ('37' , 'cee'),
            ('38' , 'cuu'),
            ('39' , 'cuu1'),
            ('40' , 'cdd'),
            ('41' , 'cdd1'),
            ('42' , 'ceu'),
            ('43' , 'ced'),
            ('44' , 'cud1'),
            ('45' , 'cud8'),
            ('46' , 'cle'),
            ('47' , 'clu'),
            ('48' , 'cld'),
            ('49' , 'cqe'),
            ('50' , 'cqu1'),
            ('51' , 'cqu8'),
            ('52' , 'cqd1'),
            ('53' , 'cqd8'),
            ('54' , 'cledqRe'),
            ('55' , 'cquqd1Re'),
            ('56' , 'cquqd11Re'),
            ('57' , 'cquqd8Re'),
            ('58' , 'cquqd81Re'),
            ('59' , 'clequ1Re'),
            ('60' , 'clequ3Re')]
    for param in params:
        if param[0] not in switchOn : continue 

        process_name = 'Zjj_'+param[1] +'_LI'
        path = os.getcwd()
        try:
            # create folder for gridpack
            os.mkdir(path + '/'+process_name)
            os.chdir(path + '/'+process_name)

            # create custimizedcards
            with open(process_name+'_custimizecards.dat', "w") as file:
                file.write('set param_card SMEFT ' + param[0] + ' 1.0\n')
            
            # create extramodels
            copyfile(path + '/prova_cW/extramodels.dat', path + '/' + process_name + '/'+ process_name+'_extramodels.dat')

            # create proc_card
            begin_lines = ['set group_subprocesses Auto\n',
            'set ignore_six_quark_processes False\n',
            'set loop_optimized_output True\n',
            'set complex_mass_scheme False\n']

            middle_lines = ['define p = g u c d s b u~ c~ d~ s~ b~\n',
            'define j = p\n',
            'define l+ = e+ mu+ ta+\n',
            'define l- = e- mu- ta-\n',
            'define vl = ve vm vt\n',
            'define vl~ = ve~ vm~ vt~\n']
            with open(process_name+'_proc_card.dat', "w") as file:
                file.writelines(begin_lines)
                file.write('import model SMEFTsim_U35_MwScheme_UFO-' + param[1] + '_massless\n')
                file.writelines(middle_lines)
                file.write('generate p p > l+ l- j j QED=4 QCD=0 SMHLOOP=0 NP=1 NP^2==1\n')
                file.write('output '+process_name+'\n')


            # create extramodels
            copyfile(path + '/prova_cW/run_card.dat', path + '/' + process_name + '/'+ process_name+'_run_card.dat')
            os.chdir(path)
        except:
            print('Directory already created')
        finally:
           try:
               copytree(path+ '/' + process_name, path + '/' + 'genproductions/bin/MadGraph5_aMCatNLO/' + process_name)    
               print('Copied directory to genproductions')
           except:
               print("Directory already in genproductions")
        os.chdir(path + '/genproductions/bin/MadGraph5_aMCatNLO/')
        # subprocess.call('./gridpack_generation.sh {} {}'.format(process_name,process_name), shell=True)
        subprocess.call('./submit_condor_gridpack_generation.sh {} {}'.format(process_name,process_name), shell=True)
        os.chdir(path)

        process_name = 'Zjj_'+param[1] +'_QU'
        path = os.getcwd()
        try:
            # create folder for gridpack
            
            os.mkdir(path + '/'+process_name)
            os.chdir(path + '/'+process_name)

            # create custimizedcards
            with open(process_name+'_custimizecards.dat', "w") as file:
                file.write('set param_card SMEFT ' + param[0] + ' 1.0\n')
            
            # create extramodels
            copyfile(path + '/prova_cW/extramodels.dat', path + '/' + process_name + '/'+ process_name+'_extramodels.dat')

            # create proc_card
            begin_lines = ['set group_subprocesses Auto\n',
            'set ignore_six_quark_processes False\n',
            'set loop_optimized_output True\n',
            'set complex_mass_scheme False\n']

            middle_lines = ['define p = g u c d s b u~ c~ d~ s~ b~\n',
            'define j = p\n',
            'define l+ = e+ mu+ ta+\n',
            'define l- = e- mu- ta-\n',
            'define vl = ve vm vt\n',
            'define vl~ = ve~ vm~ vt~\n']
            with open(process_name+'_proc_card.dat', "w") as file:
                file.writelines(begin_lines)
                file.write('import model SMEFTsim_U35_MwScheme_UFO-' + param[1] + '_massless\n')
                file.writelines(middle_lines)
                file.write('generate p p > l+ l- j j QED=4 QCD=0 SMHLOOP=0 NP=1 NP^2==2\n')
                file.write('output '+process_name+'\n')


            # create extramodels
            copyfile(path + '/prova_cW/run_card.dat', path + '/' + process_name + '/'+ process_name+'_run_card.dat')
            os.chdir(path)
        except:
            print('Directory already created')
        finally:
            try:
                copytree(path+ '/' + process_name, path + '/' + 'genproductions/bin/MadGraph5_aMCatNLO/' + process_name)    
                print('Copied directory to genproductions')
            except:
                print("Directory already in genproductions")
        os.chdir(path + '/genproductions/bin/MadGraph5_aMCatNLO/')
        #subprocess.call('./gridpack_generation.sh {} {}'.format(process_name,process_name), shell=True)
        subprocess.call('./submit_condor_gridpack_generation.sh {} {}'.format(process_name,process_name), shell=True)
        os.chdir(path)
        
