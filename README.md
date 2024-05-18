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
     
   - Após iniciar o cliente, você será solicitado a fornecer algumas configurações específicas para a conexão:

     - **Endereço IP do Servidor gRPC:** Você deve inserir o endereço IP do servidor onde o servidor gRPC está sendo executado. Por exemplo, se o servidor estiver sendo executado em uma máquina local, você pode usar `127.0.0.1` ou o endereço IP externo se estiver em outra máquina.
       
     - **Porta do Servidor gRPC:** Insira a porta na qual o servidor gRPC está escutando. O valor padrão geralmente é `50051`, a menos que você tenha configurado uma porta diferente.
       
     - **Quantas Repetições Deseja Executar:** Indique quantas vezes você deseja que o teste seja repetido. Isso é útil para executar múltiplas iterações e obter uma média de desempenho.

5. **Análise de Resultados:**
   - Observe os resultados impressos em ambos os terminais para verificar se tudo está funcionando corretamente.
