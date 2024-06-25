Encurtador de URL com Flask e SQLite

Este é um simples encurtador de URL desenvolvido usando Python com Flask e SQLite para armazenamento local. O projeto permite encurtar URLs longas para URLs curtas personalizadas.

Funcionalidades:
Encurtamento de URL: Recebe uma URL longa via JSON e a converte em uma URL curta única.
Redirecionamento: Redireciona usuários da URL curta para a URL original correspondente.
Armazenamento em SQLite: Utiliza um banco de dados SQLite para armazenar pares de URL original e URL curta.

Pré-requisitos:
Python 3
Flask
SQLite

Como inicializar o projeto:
Copiar código
python app.py
Exemplo de uso:
Para encurtar uma URL, faça uma solicitação POST para http://localhost:5000/encurtar com o seguinte corpo JSON:

json
Copiar código
{
    "url": "https://sampaiodev.com/"
}
Isso retornará a URL curta gerada. Você pode então acessar http://localhost:5000/<short_name> para ser redirecionado para a URL original.

Observações:
Este projeto é destinado apenas para uso local. Para implantação em produção, é necessário configurar um banco de dados e servidor web adequados.
O código está configurado para usar SQLite como banco de dados padrão.
