<template>  
    <head>
        <link rel="preconnect" href="https://fonts.googleapis.com">
        <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
        <link href="https://fonts.googleapis.com/css2?family=Lato:ital,wght@1,300&display=swap" rel="stylesheet">
    </head>
<div class="primeira">
    <form class="form">
        <img class="profile">
        <h1>Faça seu login ou cadastre-se</h1>
            <label>
              
                <input type="hidden" name="id" id="id" v-model="id">
                <input type="email" name="email" placeholder="e-mail" v-model="emailDigitado" class="placeholders">
                
            </label>
            <label>              
                <input type="password" name="password" placeholder="senha" v-model="senhaDigitada" class="placeholders">
            </label>
      
            <button @click="enviarLogin" class="submit" type="button" id="entrar">Entrar</button>
            <button class="submit" type="button" id="cadastrar">Cadastrar</button>
        </form>
</div>
<!-- <div class="segunda">
    <form class="form">
        <h1>Logar</h1>
            <label>
                <span>E-mail</span>
                <input type="email" name="email">
                
            </label>
            <label>
                <span>Senha</span>
                <input type="password" name="password">
            </label>
      
            <button class="submit" type="button">Logar</button>
    </form>
</div> -->
</template>

<script>
    export default{
        data(){
            return {
            emailDigitado: '',
            senhaDigitada: '',
        };
        },
        enviarLogin() {
            // Monta a URL com os parâmetros de consulta
            const url = './back-py/read-user.py';

            // Exemplo de requisição GET usando o Axios
            this.axios.get(url)
                .then(response => {
                    console.log(response.data);
                })
                .catch(error => {
                    console.error(error);
                });
        }
    }
</script>

<style scoped>

body{
    background-color: rgb(255, 255, 255);
    
}
.primeira{
    width: 498px;
    height: 696px;
    background-color: white;
    display: flex;
    align-items: center;
    justify-content: center;
    margin-left: 600px;
    margin-right: 300px;
    margin-top: 100px;
    border-radius: 30px;
}
.placeholders{
    background-color: #DFDFDF;
    display: flex;
    padding: 10px;
    margin-bottom: 30px;
    border-color: transparent;
    border-radius: 30px;
    width: 300px;
    font-size: 20px;
  
}
#entrar {
    background-color: #0CA7FF;
    color: white;
    display: flex;
    border-color: transparent;
    border-radius: 30px;
    font-family: 'Montserrat', sans-serif;
    width: 120px;
    height: 40px;
    font-size: 16px;
    margin-bottom: 10px;
    justify-content: center;
    align-items: center;
    font-weight: bold;
   
}
#cadastrar {
    background-color: #ff0cd6;
    color: white;
    display: flex;
    border-color: transparent;
    border-radius: 30px;
    font-family: 'Montserrat', sans-serif;
    width: 120px;
    height: 40px;
    font-size:16px;
    margin-bottom: 10px;
    justify-content: center;
    align-items: center;
    font-weight: bold;
}

/* Adicionando estilos para centralizar os botões */
.form {
    display: flex;
    flex-direction: column;
    align-items: center; /* Centraliza os itens horizontalmente */
    justify-content: center; /* Centraliza os itens verticalmente */
    height: 100vh; /* Isso é opcional, define a altura do formulário para ocupar a altura da tela inteira */
}


h1{
    color: #7D7D7D;
    font-size: 18px;
    display: flex;
    align-items: center;
    justify-content: center;
    margin-left: 10px;
    margin-bottom: 40px;
    font-family: 'Montserrat', sans-serif;
    font-weight: 600;
}
</style>