from .mnist_gluon_model import run_mnist_gluon_model
from tornasole.mxnet.hook import TornasoleHook as t_hook
from tornasole.mxnet import Collection, SaveConfig, reset_collections
import tornasole.mxnet as tm
from datetime import datetime
import shutil

def test_hook_custom_collection():
  reset_collections()
  tm.get_collection('ReluActivation').include(["relu*", "input_*"])
  save_config = SaveConfig(save_steps=[0,1,2,3])
  run_id = 'trial_' + datetime.now().strftime('%Y%m%d-%H%M%S%f')
  out_dir = './newlogsRunTest/' + run_id
  hook = t_hook(out_dir=out_dir, save_config=save_config, include_collections=['ReluActivation'])
  run_mnist_gluon_model(hook=hook, num_steps_train=10, num_steps_eval=10)
  shutil.rmtree(out_dir)
