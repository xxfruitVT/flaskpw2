# import Flask module
from flask import Flask, render_template, request, redirect, url_for, flash
# create Flask app intance
app = Flask(__name__, template_folder='views')
#define route for the root URL
@app.route('/')
def hello_world():
    return 'Hello,World!'
#define route for a template rendering
@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/pmb', methods=['GET', 'POST'])
def pmb():
    if request.method == 'POST':
        nama = request.form.get('nama')
        email = request.form.get('email')
        tempat_lahir = request.form.get('tempat_lahir')
        tanggal_lahir = request.form.get('tanggal_lahir')
        asal_sma = request.form.get('asal_sma')
        no_hp = request.form.get('no_hp')
        foto = request.files.get('foto')

        if foto and foto.filename != '':
            filename = secure_filename(foto.filename)
            foto.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            flash(f"Pendaftaran {nama} berhasil! Foto disimpan sebagai {filename}")
        else:
            flash("Upload foto gagal. Harap pilih file gambar.")

        return redirect(url_for('pmb'))
    return render_template('pmb.html', title="Penerimaan Mahasiswa Baru")

@app.route('/main')
def main():
    return render_template('main.html')

# run the app
if __name__ == '__main__':
    app.run(debug=True)
    