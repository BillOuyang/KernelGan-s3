import os
import tqdm

from configs import Config
from data import DataGenerator
from kernelGAN import KernelGAN
from learner import Learner


def train(conf):
    gan = KernelGAN(conf)
    learner = Learner()
    data = DataGenerator(conf, gan)
    for iteration in tqdm.tqdm(range(conf.max_iters), ncols=60):
        [g_in, d_in] = data.__getitem__(iteration)
        gan.train(g_in, d_in)
        learner.update(iteration, gan)
    gan.finish()


def main():

    import argparse

    prog = argparse.ArgumentParser()
    prog.add_argument('--input-dir', '-i', type=str, default='input_image', help='path to image input directory.')
    prog.add_argument('--output-dir', '-o', type=str, default='results', help='path to image output directory.')
    prog.add_argument('--X4', action='store_true', help='The wanted SR scale factor')
    prog.add_argument('--SR', action='store_true', help='when activated - ZSSR is performed')
    prog.add_argument('--real', action='store_true', help='ZSSRs configuration is for real images')
    args = prog.parse_args()


    for filename in os.listdir(os.path.abspath(args.input_dir)):
        conf = Config().parse(create_params(filename, args))
        # conf.img_name = filename
        # conf.input_image_path = 'input_image'
        # conf.output_dir_path = 'Results' + '\im_0_sf_4_4'
        train(conf)
    prog.exit(0)


def create_params(filename, args):
    params = ['--input_image_path', os.path.join(args.input_dir, filename),
              '--output_dir_path', os.path.abspath(args.output_dir)]
    if args.X4:
        params.append('--X4')
    if args.SR:
        params.append('--do_ZSSR')
    if args.real:
        params.append('--real_image')
    params.append('--do_ZSSR')
    params.append('--real_image')
    return params


if __name__ == '__main__':
    main()
