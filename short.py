from flask import Flask, request, redirect, jsonify
import sqlite3

app = Flask(__name__)

# Configuração do banco de dados (usando SQLite neste exemplo)
DATABASE = 'url_shortener.db'

# Função para criar a tabela 'urls' se não existir
def create_table():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS urls
                      (id INTEGER PRIMARY KEY AUTOINCREMENT, original_url TEXT NOT NULL, short_name TEXT UNIQUE NOT NULL)''')
    conn.commit()
    conn.close()

# Chama a função para criar a tabela ao iniciar o aplicativo
create_table()

# Rota para encurtar uma URL
@app.route('/encurtar', methods=['POST'])
def encurtar_url():
    original_url = request.json.get('url')  # Assume que a URL original é passada via JSON
    if not original_url:
        return jsonify({'error': 'URL não fornecida'}), 400

    short_name = 'Sampaio'

    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    # Verifica se o nome curto já existe no banco de dados
    cursor.execute('SELECT original_url FROM urls WHERE short_name=?', (short_name,))
    row = cursor.fetchone()
    if row:
        # Se já existir, atualiza a URL original associada ao nome curto
        cursor.execute('UPDATE urls SET original_url=? WHERE short_name=?', (original_url, short_name))
    else:
        # Insere a nova URL no banco de dados com o nome curto 'Sampaio'
        cursor.execute('INSERT INTO urls (original_url, short_name) VALUES (?, ?)', (original_url, short_name))
    
    conn.commit()
    conn.close()

    # Retorna a URL curta gerada
    short_url = f'http://localhost:5000/{short_name}'
    return jsonify({'short_url': short_url})

# Rota para redirecionar para a URL original com base no nome curto
@app.route('/<short_name>')
def redirect_to_url(short_name):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    # Busca a URL original com base no nome curto
    cursor.execute('SELECT original_url FROM urls WHERE short_name=?', (short_name,))
    row = cursor.fetchone()
    if row:
        original_url = row[0]
        conn.close()
        return redirect(original_url, code=302)
    else:
        conn.close()
        return jsonify({'error': 'URL não encontrada'}), 404

if __name__ == '__main__':
    app.run(debug=True)




# EXEMPLO DE URL A INSERIR 
# $url = "http://localhost:5000/encurtar"
# $headers = @{
#     "Content-Type" = "application/json"
# }
# $body = '{"url": "https://sampaiodev.com/"}'

# $response = Invoke-RestMethod -Uri $url -Method Post -Headers $headers -Body $body
# $response


