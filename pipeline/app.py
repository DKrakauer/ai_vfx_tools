from flask import Flask, render_template, request, send_file, after_this_request
from dotenv import load_dotenv
from driver import generate_vfx
import shutil
import zipfile
from io import BytesIO
import os

app = Flask(__name__)

load_dotenv()
data = ""
highlighted_content = ""
flag = 0
current_iteration = 0

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload():
    # Get textbox from the form
    global current_iteration
    prompt = request.form.get('textbox')
    current_iteration += 1
    generate_vfx(prompt, current_iteration)

    #return
    return render_template('download.html', message = "Done!")


@app.route('/download', methods=['POST'])
def download():
    # defining the directory.
    dir_name = "./output/"
    archive_name = 'output_files'
    
    try: 
        # create a Zip file that includes every file from the specified directory.
        shutil.make_archive(archive_name, 'zip', dir_name)

        # moving archive to a specific path
        shutil.move(f'{archive_name}.zip', dir_name)

        # send the created zip file to the client.
        return send_file(f'{dir_name}/{archive_name}.zip', as_attachment=True)
    except Exception as e:
        return str(e)
    finally:
        # clear the 'output' directory. 
        for filename in os.listdir(dir_name):
            file_path = os.path.join(dir_name, filename)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
            except Exception as e:
                print(f'Failed to delete {file_path}. Reason: {e}')

@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/privacy')
def privacy():
    return render_template('privacy.html')


@app.route('/terms')
def terms():
    return render_template('terms_and_conditions.html')


@app.route("/teamcot")
def teamcot():
    return render_template("teamcot.html")


@app.route("/cot")
def cot():
    return render_template("cot.html")


@app.route("/aboutplagiarism")
def aboutplagiarism():
    return render_template("aboutplagiarism.html")

if __name__ == '__main__':
    app.run(debug=True)
