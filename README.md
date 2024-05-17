# Exercício de Remote Procedure Call (RPC) como mecanismo de comunicação

### Computação Escalável


> ## Grupo
>
> - Dávila Meireles
> - Dominique de Vargas de Azevedo
> - Lívia Verly
> - Pedro Thomaz Conzatti Martins
> - Thiago Franke Melchiors


## Instruções de Execução

Siga os passos abaixo para configurar e executar o ambiente do projeto:

1. **Clonar o Repositório:**
   - Abra o terminal e clone o repositório usando o comando:
     ```
     git clone https://github.com/pedrothomazm/exercicio-rpc
     ```

2. **Instalar Dependências:**
   - Navegue para o diretório do projeto clonado e instale as bibliotecas necessárias:
     ```
     cd exercicio-rpc
     pip install -r requirements.txt
     ```

3. **Iniciar o Servidor:**
   - Ative o servidor executando o stub do servidor. Certifique-se de estar no diretório correto do projeto:
     ```
     python cade_analytics_mock/cade_analytics_server.py
     ```

4. **Iniciar o Cliente:**
   - Em um novo terminal, navegue novamente para o diretório do projeto e inicie o cliente:
     ```
     python cade_analytics_mock/cade_analytics_client.py
     ```

5. **Análise de Resultados:**
   - Observe os resultados impressos em ambos os terminais para verificar se tudo está funcionando corretamente.
