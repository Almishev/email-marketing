import smtplib
import os
import sys
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email import encoders
import argparse

# Настройки за имейл сървъра
EMAIL_HOST = "mail.privateemail.com"
EMAIL_PORT = 587
EMAIL_USER = "admin@pirinpixel.com"
EMAIL_PASS = "asroma"

def send_email(recipient_email, subject="Специални предложения от semma.bg", 
               sender_email=EMAIL_USER, sender_password=EMAIL_PASS,
               smtp_server=EMAIL_HOST, smtp_port=EMAIL_PORT):
    """
    Изпраща HTML имейл шаблон на посочения получател
    
    Args:
        recipient_email (str): Имейл адрес на получателя
        subject (str): Тема на имейла
        sender_email (str): Имейл адрес на изпращача
        sender_password (str): Парола на изпращача
        smtp_server (str): SMTP сървър
        smtp_port (int): SMTP порт
    
    Returns:
        bool: True ако изпращането е успешно, False при грешка
    """
    try:
        # Зареждане на HTML шаблона
        template_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "index.html")
        with open(template_path, 'r', encoding='utf-8') as file:
            html_content = file.read()
        
        # Създаване на MIME обект
        message = MIMEMultipart()
        message['Subject'] = subject
        message['From'] = sender_email
        message['To'] = recipient_email
        
        # Прикачване на HTML съдържанието
        html_part = MIMEText(html_content, 'html', 'utf-8')
        message.attach(html_part)
        
        # Изпращане на имейла
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.send_message(message)
            print(f"Имейлът е успешно изпратен до {recipient_email}!")
            return True
            
    except Exception as e:
        print(f"Грешка при изпращане на имейла: {e}")
        return False

def send_bulk_emails(recipients_file, subject="Специални предложения от semma.bg", 
                    sender_email=EMAIL_USER, sender_password=EMAIL_PASS,
                    smtp_server=EMAIL_HOST, smtp_port=EMAIL_PORT):
    """
    Изпраща имейли на група получатели от текстов файл
    
    Args:
        recipients_file (str): Път до файл с имейли (по един на ред)
        subject (str): Тема на имейла
        sender_email (str): Имейл адрес на изпращача
        sender_password (str): Парола на изпращача
        smtp_server (str): SMTP сървър
        smtp_port (int): SMTP порт
    
    Returns:
        tuple: (брой успешни, брой неуспешни)
    """
    successful = 0
    failed = 0
    
    try:
        with open(recipients_file, 'r') as file:
            recipients = [line.strip() for line in file if line.strip() and not line.strip().startswith('#')]
            
        total = len(recipients)
        print(f"Започва изпращане на имейли до {total} получатели...")
        
        for i, recipient in enumerate(recipients):
            print(f"[{i+1}/{total}] Изпращане към {recipient}...")
            if send_email(recipient, subject, sender_email, sender_password, smtp_server, smtp_port):
                successful += 1
            else:
                failed += 1
                
        print(f"\nРезултати:\nУспешно изпратени: {successful}\nНеуспешни: {failed}")
        return (successful, failed)
        
    except Exception as e:
        print(f"Грешка при масово изпращане: {e}")
        return (successful, failed)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Изпращане на маркетингови имейли')
    parser.add_argument('--recipient', '-r', help='Имейл адрес на получателя')
    parser.add_argument('--file', '-f', help='Файл с имейл адреси')
    parser.add_argument('--subject', '-s', default='Специални предложения от semma.bg', help='Тема на имейла')
    parser.add_argument('--sender', default=EMAIL_USER, help='Имейл адрес на изпращача')
    parser.add_argument('--password', '-p', default=EMAIL_PASS, help='Парола')
    parser.add_argument('--server', default=EMAIL_HOST, help='SMTP сървър')
    parser.add_argument('--port', type=int, default=EMAIL_PORT, help='SMTP порт')
    
    args = parser.parse_args()
    
    if args.file:
        send_bulk_emails(args.file, args.subject, args.sender, args.password, args.server, args.port)
    elif args.recipient:
        send_email(args.recipient, args.subject, args.sender, args.password, args.server, args.port)
    else:
        print("Трябва да посочите получател (--recipient) или файл с получатели (--file)")
        parser.print_help()