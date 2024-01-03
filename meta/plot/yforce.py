import meta
from meta import utils
import os

models = utils.get_models('all')
path = None
for model in models:
    if model.id == 0:
        path = model.name
        break  # 停止循环，因为已经找到 ID 为 0 的模型

if path is not None:
    print(f"ID为0的模型的名称是：{path}")
    directory = os.path.dirname(path)

    utils.MetaCommand(f"read dis Dyna3d {path} All Displacements")

    title = "rcforc"
    utils.MetaCommand(f"xyplot create {title}")
    utils.MetaCommand(f"window active {title}")
    utils.MetaCommand(f"xyplot model active all")
    utils.MetaCommand(f"xyplot model load binout {directory}/binout0000")
    utils.MetaCommand(f"xyplot read lsdyna {title} {directory}/binout0000 rcforc-Master all Y_force_(yf)")
    utils.MetaCommand(f"window autotile")
    utils.MetaCommand(f"xyplot plotoptions title set {title} 0 """)


