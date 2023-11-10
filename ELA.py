import os
import subprocess

def ela_analysis(input_folder, output_folder):
    # Create output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Iterate through all frames in the input folder
    for filename in os.listdir(input_folder):
        if filename.endswith(".png"):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, f"ela_{filename}")

            # Perform ELA using ImageMagick command line
            command = f"magick convert {input_path} -scale 50% -quality 85 -background white -flatten -difference {output_path}"
            subprocess.run(command, shell=True, check=True)

            print(f"ELA analysis completed for {filename}")

if __name__ == "__main__":
    # Replace 'output_frames' with the path to the folder containing the frames
    input_frames_folder = 'output_frames'

    # Replace 'ela_output' with the desired output folder for ELA images
    output_ela_folder = 'ela_output'

    ela_analysis(input_frames_folder, output_ela_folder)
