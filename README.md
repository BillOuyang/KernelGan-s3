# Blind SR Kernel Estimation with scale factor of 3 using an Internal-GAN
# "KernelGAN"
### Bojun Ouyang, Junyi Zhou


Paper: https://arxiv.org/abs/1909.06581




## Usage:




### Generate your own data:
In order to generate the LR images from your own HR images such that its width and height will be 1/3 of the HR images, run the files under the ```datagenerator``` folder:

    1) put your HR images under the 'datagenerator/input_image' folder, the images must be in jpg format!
    
    2) run the 'generator.py' file, this will generate the LR images by first applying a
       a randomly sample gaussian kernel then downsampling by 3.
     
    3) The kenel(ground truth) and the LR images will be under the 'datagenerator/output_kernel' folder
 


### Quick usage on your data:  
Put your LR images in the ```input_image``` folder, run the ```train.py``` file. 
It will generate the predicted kernel and HR images in the ```Results``` folder.





