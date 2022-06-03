import os


PATH_BASE = os.path.dirname(os.path.abspath(__file__))
IMG_PATH = os.path.join(PATH_BASE,'..','data','image')
LABEL_PATH = os.path.join(PATH_BASE,'..','data','label')
DATA_PATH = os.path.join(PATH_BASE,'..','data')

nc = 13

DATA ={
    'class':
 ['Potato chips', 'Sprite', 'Coke', 'Grape juice', 'Apple', 'Orange', 'Orange juice', 'Chocolate drink', 'Sausage', 'Pringle', 'Cracker', 'Noodles', 'Milk']
}

MODEL = { 'anchors':[[(1.25, 1.625), (2.0, 3.75), (4.125, 2.875)],
                    [(1.875, 3.8125), (3.875, 2.8125), (3.6875, 7.4375)],
                    [(3.625, 2.8125), (4.875, 6.1875), (11.65625, 10.1875)]],
          'strides':[8,16,32],
          'anchor_pre_scale':3
}

TRAIN = {
            'train_img_size':448,
            'augment':True,
            'batch_size':4,
            'mult_scale_train':True,
            'IoU_threshold_loss':0.5,
            'epoch':50,
            'work_num':4,
            'momentum':0.9,
            'weight_decay':0.0005,
            'lr_init':1e-4,
            'lr_end':1e-6,
            'warm_epoch':2
}

TEST = {
        'test_img_size':448,
        'work_num':4,
        'batch_size':4,
        'NMS_threshold':0.5,
        'multi_scale_test':False,
        'flip_test':False
}
