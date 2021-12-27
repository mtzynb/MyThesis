import codes.utility as utility
import codes.feature_selection.wrapper_methods.plot_wrapper_f_selection as plot_fsf

sfs_model = utility.load_model("50_combined_90_model.sav")
print("model loaded!")
# --------------------save plot----------------------------
plot_fsf.plot_f_selection3(sfs_model,
                           'Sequential Forward Selection Plot with 50 Selected Features',
                           'new_50_combined_90_sfs_plot.png',
                           feature_no=50,
                           x_lable_steps=5)
print("plot saved.")
# --------------------------------------------------
