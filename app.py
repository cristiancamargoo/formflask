from flask import Flask, render_template, request, redirect, url_for, session
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email

app = Flask(__name__, template_folder='C:/Users/cristian_a_oliveira/Documents/DSWE/web_forms_wtf/templates')

app.config['SECRET_KEY'] = 'chave_secreta'

class ContatoForm(FlaskForm):
    nome = StringField(
        'Nome',
        validators=[DataRequired()]
    )
    
    email = StringField(
        'Email',
        validators=[DataRequired(), Email()]
    )
    
    idade = IntegerField(
        'Idade',
        validators=[DataRequired()]
    )
    
    mensagem = TextAreaField(
        'Mensagem',
        validators=[DataRequired()]
    )

    enviar = SubmitField(
        'Enviar'
    )

@app.route('/', methods=['GET', 'POST'])
def index():
    formulario = ContatoForm()
    if formulario.validate_on_submit():
        contato = {
            'nome': formulario.nome.data,
            'email': formulario.email.data,
            'idade': formulario.idade.data,
            'mensagem': formulario.mensagem.data
        }

        session['contato'] = contato

        return redirect(url_for('obrigado'))
    
    return render_template('formulario.html', formulario=formulario)

@app.route('/obrigado')
def obrigado():
    contato = session.get('contato', None)

    if contato is None:
        return redirect(url_for('index'))
    
    session.clear()

    return render_template('obrigado.html', contato=contato)

if __name__ == '__main__':
    app.run(debug=True)
