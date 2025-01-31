#  DC_pars_M100.py:    parameters for M100
#
#  to work with, and edit parameters here, copy this script to DC_pars.py to be used by your DC_script.py

#  Data and procedure are described here:
#        https://casaguides.nrao.edu/index.php?title=M100_Band3_Combine_5.4

step_title = {0: 'Concat',
              1: 'Prepare the SD-image',
              2: 'Clean for Feather/Faridani',
              3: 'Feather', 
              4: 'Faridani short spacings combination (SSC)',
              5: 'Hybrid (startmodel clean + Feather)',
              6: 'SDINT',
              7: 'TP2VIS',
              8: 'Assessment of the combination results'
              }

#thesteps=[0,1,2,3,4,5,6,7,8]
thesteps=[0,1,5]

######## collect only the product name (i.e. run assessment on already existing combination products)?          
dryrun = False    # False to execute combination, True to gather filenames only


# this script assumes the DC_locals.py has been execfiled'd - see the README.md how to do this

pathtoconcat = _s4p_data #+ '/M100/'
pathtoimage  = _s4p_work + '/M100/'



# to quote the casaguide, "In order to run this guide you will need the following three files:"
_7ms  = '/M100_Band3_7m_CalibratedData/M100_Band3_7m_CalibratedData.ms'
_12ms = '/M100_Band3_12m_CalibratedData/M100_Band3_12m_CalibratedData.ms'
_sdim = '/M100_Band3_ACA_ReferenceImages_5.1/M100_TP_CO_cube.spw3.image.bl'



# setup for concat (the optional step 0)

a12m=[pathtoconcat + _12ms
     ]
      
weight12m = [1.]
        
a7m =[pathtoconcat + _7ms
     ]

weight7m = [1.]  # weigthing for REAL data !  If CASA calibration older than 4.3.0: weight: 0.193



skymodel=''    # model used for simulating the observation, expected to be CASA-imported



#  the concatenated MS 
concatms     = pathtoimage + 'M100-B3.alma.all_int-weighted.ms' 




############# input to combination methods ###########

vis            = ''                                 # set to '' is concatms is to be used, else define your own ms-file
sdimage_input  = pathtoconcat + _sdim
imbase         = pathtoimage + 'M100-B3'            # path + image base name
sdbase         = pathtoimage + 'M100-B3'            # path + sd image base name


# TP2VIS related:
TPpointingTemplate = a12m[0]
listobsOutput      = imbase+'.12m.log'
TPpointinglist     = imbase+'.12m.ptg'
TPpointinglistAlternative = 'user-defined.ptg' 

TPnoiseRegion   = '150,200,150,200'  # in unregridded SD image (i.e. sdreordered = sdbase +'.SD_ro.image')
TPnoiseChannels = '1~7'              # in unregridded and un-cut SD cube (i.e. sdreordered = sdbase +'.SD_ro.image')!



######## names and parameters that should be noted in the file name ######

# structure could be something like:
#    imname = imbase + cleansetup + combisetup 

mode     = 'cube'      # 'mfs' or 'cube'
mscale   = 'MS'       # 'MS' (multiscale) or 'HB' (hogbom; MTMFS in SDINT by default!)) 
masking  = 'SD-AM'    # 'UM' (user mask), 'SD-AM' (SD+AM mask)), 'AM' ('auto-multithresh') or 'PB' (primary beam)
inter    = 'nIA'      # interactive ('IA') or non-interactive ('nIA')
nit     = 10#1000000           # max = 9.9 * 10**9 

specsetup =  'INTpar' # 'SDpar' (use SD cube's spectral setup) or 'INTpar' (user defined cube setup)
######### if "SDpar", want to use just a channel-cut-out of the SD image? , 
# else set to None (None automatically for 'INTpar'
startchan = 30  #None  # start-value of the SD image channel range you want to cut out 
endchan   = 39  #None  #   end-value of the SD image channel range you want to cut out




# resulting name part looks like
# cleansetup = '.'+ mode +'_'+ specsetup +'_'+ mscale +'_'+ masking +'_'+ inter +'_n'+ str(nit)


######### specific inputs for masking  = 'SD-AM', else ignore

smoothing = 5    # smoothing of the threshold mask (by 'smoothing x beam')
RMSfactor = 0.5  # continuum rms level (not noise from emission-free regions but entire image)
cube_rms = 3     # cube noise (true noise) x this factor
cont_chans =''   # line free channels for cube rms estimation
sdmasklev = 0.3  # maximum x this factor = threshold for SD mask


momchans = '8~63' #line-free: '1~7,64~69'      # channels to compute moment maps (integrated intensity, etc.) 

                     
########## general tclean parameters

t_spw         = '' 
t_field       = ''
t_imsize      = 560  
t_cell        = '0.5arcsec' 
t_phasecenter = 'J2000 12h22m54.9 +15d49m15'             
t_start       = '1400km/s' #'1550km/s', #'1400km/s',  
t_width       = '5km/s'  
t_nchan       = 70 #10, #70,  
t_restfreq    = '115.271202GHz'
t_threshold   = ''               # SDINT: None 
t_maxscale    = -1 #10.              # recommendations/explanations 
t_mask        = '' 
t_pbmask      = 0.4
t_sidelobethreshold = 2.0 
t_noisethreshold    = 4.25 
t_lownoisethreshold = 1.5               
t_minbeamfrac       = 0.3 
t_growiterations    = 75 
t_negativethreshold = 0.0 
 

########## sdint parameters

sdpsf   = ''
dishdia = 12.0         
                 

########### SD-AM masks for all methods using tclean etc.:                       

# options: 'SD', 'INT', 'combined'

tclean_SDAMmask = 'INT'  
hybrid_SDAMmask = 'INT'     
sdint_SDAMmask  = 'INT'     
TP2VIS_SDAMmask = 'INT'     

       
########### SD factors for all methods:                       
               
sdfac   = [1.0]          # feather parameter
SSCfac  = [1.0]          # Faridani parameter
sdfac_h = [1.0]          # Hybrid feather paramteter
sdg     = [1.0]          # SDINT parameter
TPfac   = [1.0]          # TP2VIS parameter
          

          

