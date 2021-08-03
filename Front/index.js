const express = require('express');
const session = require('express-session');
const bodyParser = require('body-parser');
const axios = require('axios');

const port = 3000;
var path = require('path');
const app = express();

var backend = 'http://localhost:3001'

app.use(session({secret:'asdasdasdasdas'}));
app.use(bodyParser.urlencoded({extend:true}));
app.use(bodyParser.json());
app.engine('html', require('ejs').renderFile);
app.set('view engine', 'html');
app.set('views', path.join(__dirname, '/views'));


app.get('/',(req, res)=>{
    res.render('index');
});

app.post('/buscar',(req, res)=>{
    origem = req.body.origem;
    destino = req.body.destino;
    axios.get(backend + '/busca_largura/' + origem + '/' + destino, {
        headers:{
            ContentType: 'application/json'
        },
        validateStatus: function (status) {
            return status >= 200 && status < 300; // default
        }
    }).then((responseLargura) => {
        largura = responseLargura.data;
        axios.get(backend + '/busca_profundidade/' + origem + '/' + destino, {
            headers:{
                ContentType: 'application/json'
            },
            validateStatus: function (status) {
                return status >= 200 && status < 300; // default
            }
        }).then((responseProfundidade) => {
            profundidade = responseProfundidade.data;
            console.log(largura);
            console.log(profundidade);
            res.render('busca', {largura : largura, profundidade : profundidade} );
        }).catch(function (error){
            console.log(error);
        });
    }).catch(function (error){
        console.log(error);
    });


});


app.listen(port,()=>{
    console.log('Servidor em Execução');
});
