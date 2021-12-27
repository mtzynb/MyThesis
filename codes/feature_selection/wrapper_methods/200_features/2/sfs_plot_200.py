import codes.utility as utility
import codes.feature_selection.wrapper_methods.plot_wrapper_f_selection as plot_fsf

sfs_model = utility.load_model("200_combined_90_model.sav")
print("model loaded!")
# --------------------save plot----------------------------
plot_fsf.plot_f_selection3(sfs_model,
                           'Sequential Forward Selection Plot with 200 Selected Features',
                           'new_200_combined_90_sfs_plot.png',
                           feature_no=200,
                           x_lable_steps=20)
print("plot saved.")
# --------------------------------------------------
