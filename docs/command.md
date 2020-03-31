# Interface de comandos

- Command: Command é a interface para implementar comandos que não requerem autenticação de usuários. Você só irá precisar implementar o método `exec`.
Lembre-se de ao instanciar o seu objeto, chamar o método `load` passando a instância do bot e para executar, chamar o método `exec` passando a mensagem recebida.

```python
class RandomCommand(Command):
    def exec(self, message):
        bot = self.bot # Você já possui uma instância de bot previamente setada
        # aqui você pode fazer o que quiser pra retornar pro grupo
```

- AuthCommand: diferente de Command, AuthCommand requer que vc implemente o método `command` que será executado caso o usuário tenha permissão de acesso ao recurso acionado. Você também poderá implementar `useCustomError` que retornará `boolean`, se for verdadeiro, implemente `onError` que recebe a mensagem. Caso não implemente `useCustomError` e `onError`, o comportamento padrão será mandar uma mensagem de "Não autorizado".


```python
class DeleteUser(AuthCommand):
     def command(self, message):
        db.delete(message.from_user.id)

    def useCustomError(self):
        return True

    def onError(self, message):
        return bot.reply_to(message.reply_to_message, "Tá maluco, cara?")

```
