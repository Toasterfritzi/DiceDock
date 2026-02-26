from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, CharacterForm
from .models import Character

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = UserRegisterForm()
    return render(request, 'characters/register.html', {'form': form})

@login_required
def dashboard(request):
    characters = Character.objects.filter(user=request.user)
    return render(request, 'characters/dashboard.html', {'characters': characters})

@login_required
def create_character(request):
    if request.method == 'POST':
        form = CharacterForm(request.POST, request.FILES)
        if form.is_valid():
            character = form.save(commit=False)
            character.user = request.user
            
            # Basic handling of the equipment preference for the prototype
            pref = form.cleaned_data.get('equipment_preference')
            if pref == 'gold':
                character.gold = 100 # Default starting gold if chosen
                character.equipment = "Nichts (Startgold gewählt)"
            else:
                character.gold = 0
                character.equipment = "Standard-Ausrüstung für " + character.character_class
                
                # Populate new fields with dummy data for the prototype visualization
                character.inventory = [
                    {"name": "Potion of Healing", "quantity": 2},
                    {"name": "Rations (1 day)", "quantity": 5},
                    {"name": "Hempen Rope (50ft)", "quantity": 1},
                    {"name": "Torch", "quantity": 10},
                    {"name": "Waterskin", "quantity": 1},
                    {"name": "Tinderbox", "quantity": 1}
                ]
                character.weapons = [
                    {"name": "Longsword +1", "type": "Melee • Slashing", "hit": "+6", "damage": "1d8+4"},
                    {"name": "Javelin", "type": "Thrown (30/120) • Piercing", "hit": "+5", "damage": "1d6+3"}
                ]
                character.proficiencies = ["Athletics", "Intimidation", "Persuasion", "Heavy Armor"]
                character.spell_slots = {
                    "1": {"total": 4, "used": 2}
                }
                # Set some default values for new fields
                character.experience = 6500
                character.max_experience = 10000
                character.current_hp = 42
                character.max_hp = 54
                character.hit_dice = "5d10"
                character.armor_class = 18
                character.speed = 30
                character.silver = 42
                character.copper = 12
                character.gold = 154 # Override gold for the demo look

            character.save()
            return redirect('character_detail', pk=character.pk)
    else:
        form = CharacterForm()
    return render(request, 'characters/character_form.html', {'form': form})

@login_required
def character_detail(request, pk):
    character = get_object_or_404(Character, pk=pk, user=request.user)
    return render(request, 'characters/character_detail.html', {'character': character})
