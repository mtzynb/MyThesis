import codes.utility as utility
import codes.feature_selection.wrapper_methods.plot_wrapper_f_selection as plot_fsf
from bidi.algorithm import get_display
from arabic_reshaper import reshape

sfs_model = utility.load_model("50_combined_90_model.sav")
print("model loaded!")
# --------------------save plot----------------------------
title_ = 'نمودارانتخاب متوالی رو به جلو با انتخاب 50 ویژگی'

plot_fsf.plot_f_selection3(sfs_model,
                           get_display(reshape(title_)),
                           'new_50_combined_90_sfs_plot_farsi.png',
                           feature_no=50,
                           x_lable_steps=5)
print("plot saved.")
# --------------------------------------------------
