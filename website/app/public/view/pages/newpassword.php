<div id='form'>
    <h1>Recuperação de senha</h1>
      
    <div class="fields">
        <label for="password">Senha</label>
        <input type="password" id='password' name="password" placeholder="Senha" value='leonardo' required>
    </div>
    <div class="fields">
        <label for="password">Repita sua senha</label>
        <input type="password" id='repeat' name="repeat" placeholder="Repita sua senha" value='leonardo' required>
    </div>

    <?php

    if (isset($_GET['user'], $_GET['code'])) {
        $user = $_GET['user'];
        $code = $_GET['code'];
        echo <<<html
        
            <input type=hidden id='user' name='password' value=$user required>
            html;
        echo <<<html
            <input type=hidden id='code' name='password' value=$code required>
            html;
    }

    ?>

    <div id="entrar">
        <input type='submit' name="loginbutton" id="loginbutton" class="btn-login" onclick="cadastrar()" value="Entrar">
    </div>


    <div class="cadastro">
    </div>
</div>

<script src="./assets/js/recovery.js"></script>