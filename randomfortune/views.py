
from django.shortcuts import render
import random
# Create your views here.


# Lista de mensagens
fortuneList = [
   "All will go well with your new project.",
   "If you continually give, you will continually have.",
   "Self-knowledge is a life long process.",
   "You are busy, but you are happy.",
   "Your abilities are unparalleled.",
   "Those who care will make the effort.",
   "Now is the time to try something new.",
   "Miles are covered one step at a time.",
   "Don’t just think, act!"
]

# View para exibir a previsão
def fortune(request):
    fortune = random.choice(fortuneList)
    context = {"fortune": fortune}  # Criando o dicionário de contexto
    return render(request, "randomfortune/fortune.html", context)  # Renderizando o template


  