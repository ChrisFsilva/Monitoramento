$Username = "ti@alko.com.br";
$Password = "P-alko46321";
$SendTo = "ti@alko.com.br";
$MailServer = "email-ssl.com.br";
$HostName = $args[0];
$EndereçoIP = $args[1];
$PingStatus = $args[2];
$FailedOn = $args[3];

$mensagem = novo-objeto Net.Mail.MailMessage;
$message.From = $Nome de usuário;
$mensagem.To.Add($SendTo);
$message.Subject = "Falha de comunicação com $HostName";
$message.Body = "Informações sobre o ping com falha: `r`nNome do host: $HostName`r`nEndereço IP: $IPAddress`r`nStatus do ping: $PingStatus`r`nHora do ping: $FailedOn";

$smtp = novo-objeto Net.Mail.SmtpClient($MailServer, "465");
$smtp.EnableSSL = $true;
$smtp.Credentials = Novo objeto System.Net.NetworkCredential($Nome de usuário, $Senha);
$smtp.send($mensagem);

Read-Host -Prompt "Pressione Enter para sair"