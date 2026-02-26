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
            
            # 1. Automatisierte Werte (Standard Array: 15, 14, 13, 12, 10, 8)
            # Zuweisung basierend auf der Klasse (Primärattribute zuerst)
            stand_array = [15, 14, 13, 12, 10, 8]
            
            c_class = form.cleaned_data.get('character_class').lower()
            if 'barbar' in c_class:
                character.strength, character.constitution, character.dexterity, character.wisdom, character.charisma, character.intelligence = stand_array
                character.hit_dice = "1d12"
            elif 'bard' in c_class:
                character.charisma, character.dexterity, character.constitution, character.wisdom, character.intelligence, character.strength = stand_array
                character.hit_dice = "1d8"
            elif 'kleriker' in c_class or 'cleric' in c_class:
                character.wisdom, character.constitution, character.strength, character.charisma, character.intelligence, character.dexterity = stand_array
                character.hit_dice = "1d8"
            elif 'druid' in c_class:
                character.wisdom, character.constitution, character.dexterity, character.intelligence, character.charisma, character.strength = stand_array
                character.hit_dice = "1d8"
            elif 'kämpfer' in c_class or 'fighter' in c_class:
                character.strength, character.constitution, character.dexterity, character.wisdom, character.intelligence, character.charisma = stand_array
                character.hit_dice = "1d10"
            elif 'mönch' in c_class or 'monk' in c_class:
                character.dexterity, character.wisdom, character.constitution, character.strength, character.intelligence, character.charisma = stand_array
                character.hit_dice = "1d8"
            elif 'paladin' in c_class:
                character.strength, character.charisma, character.constitution, character.wisdom, character.dexterity, character.intelligence = stand_array
                character.hit_dice = "1d10"
            elif 'waldläufer' in c_class or 'ranger' in c_class:
                character.dexterity, character.wisdom, character.constitution, character.strength, character.intelligence, character.charisma = stand_array
                character.hit_dice = "1d10"
            elif 'schurke' in c_class or 'rogue' in c_class:
                character.dexterity, character.intelligence, character.constitution, character.charisma, character.wisdom, character.strength = stand_array
                character.hit_dice = "1d8"
            elif 'zauberer' in c_class or 'sorcerer' in c_class:
                character.charisma, character.constitution, character.dexterity, character.wisdom, character.intelligence, character.strength = stand_array
                character.hit_dice = "1d6"
            elif 'hexenmeister' in c_class or 'warlock' in c_class:
                character.charisma, character.constitution, character.dexterity, character.wisdom, character.intelligence, character.strength = stand_array
                character.hit_dice = "1d8"
            elif 'magier' in c_class or 'wizard' in c_class:
                character.intelligence, character.constitution, character.dexterity, character.wisdom, character.charisma, character.strength = stand_array
                character.hit_dice = "1d6"
            else:
                # Fallback
                character.strength, character.dexterity, character.constitution, character.intelligence, character.wisdom, character.charisma = stand_array
                character.hit_dice = "1d8"

            # 3. Hintergrund-Boni (Background Bonuses)
            # Comprehensive list of all 16 typical 2024 D&D backgrounds
            b_ground = form.cleaned_data.get('background', '').lower()
            
            if 'adeliger' in b_ground or 'noble' in b_ground:
                character.strength += 2
                character.charisma += 1
            elif 'akolyth' in b_ground or 'acolyte' in b_ground:
                character.wisdom += 2
                character.intelligence += 1
            elif 'handwerker' in b_ground or 'artisan' in b_ground:
                character.strength += 2
                character.dexterity += 1
            elif 'scharlatan' in b_ground or 'charlatan' in b_ground:
                character.charisma += 2
                character.dexterity += 1
            elif 'krimineller' in b_ground or 'criminal' in b_ground:
                character.dexterity += 2
                character.intelligence += 1
            elif 'unterhalter' in b_ground or 'entertainer' in b_ground:
                character.charisma += 2
                character.dexterity += 1
            elif 'bauer' in b_ground or 'farmer' in b_ground or 'peasant' in b_ground:
                character.constitution += 2
                character.wisdom += 1
            elif 'wache' in b_ground or 'guard' in b_ground:
                character.strength += 2
                character.wisdom += 1
            elif 'fremder' in b_ground or 'guide' in b_ground or 'outlander' in b_ground:
                character.wisdom += 2
                character.dexterity += 1
            elif 'einsiedler' in b_ground or 'hermit' in b_ground:
                character.wisdom += 2
                character.constitution += 1
            elif 'händler' in b_ground or 'merchant' in b_ground:
                character.charisma += 2
                character.intelligence += 1
            elif 'weiser' in b_ground or 'sage' in b_ground:
                character.intelligence += 2
                character.wisdom += 1
            elif 'seefahrer' in b_ground or 'sailor' in b_ground:
                character.dexterity += 2
                character.wisdom += 1
            elif 'gelehrter' in b_ground or 'scribe' in b_ground:
                character.intelligence += 2
                character.wisdom += 1
            elif 'soldat' in b_ground or 'soldier' in b_ground:
                character.strength += 2
                character.constitution += 1
            elif 'straßenkind' in b_ground or 'urchin' in b_ground or 'wayfarer' in b_ground:
                character.dexterity += 2
                character.wisdom += 1
            else:
                # Fallback bonus
                if character.character_class.lower() in ['barbar', 'kämpfer', 'paladin']:
                    character.strength += 2
                    character.constitution += 1
                elif character.character_class.lower() in ['schurke', 'mönch', 'waldläufer']:
                    character.dexterity += 2
                    character.wisdom += 1
                else:
                    character.charisma += 2
                    character.intelligence += 1

            # 4. Level 1 Base Stats Calculation
            character.level = 1
            character.experience = 0
            character.max_experience = 300 # XP for level 2

            # Calculate Max HP on Level 1: Max of hit dice + CON modifier
            hit_dice_val = int(character.hit_dice.split('d')[1])
            con_mod = (character.constitution - 10) // 2
            character.max_hp = hit_dice_val + con_mod
            
            # Race-specific HP modifications
            c_race = form.cleaned_data.get('race', '').lower()
            if 'zwerg' in c_race or 'dwarf' in c_race:
                character.max_hp += 1
                
            character.current_hp = character.max_hp
            
            # Base AC (unarmored) = 10 + DEX mod
            dex_mod = (character.dexterity - 10) // 2
            character.armor_class = 10 + dex_mod
            
            # Speed default (updated later by race)
            character.speed = 30
            if 'waldelf' in c_race or 'wood elf' in c_race:
                character.speed = 35
            elif 'goliath' in c_race:
                character.speed = 35

            character.save()
            return redirect('character_detail', pk=character.pk)
    else:
        form = CharacterForm()
    return render(request, 'characters/character_form.html', {'form': form})

@login_required
def character_detail(request, pk):
    character = get_object_or_404(Character, pk=pk, user=request.user)
    return render(request, 'characters/character_detail.html', {'character': character})

@login_required
def character_levelup(request, pk):
    character = get_object_or_404(Character, pk=pk, user=request.user)
    
    if request.method == 'POST':
        # Apply standard Level-Up logic
        character.level += 1
        
        # Calculate HP increase (Average of hit dice + CON modifier)
        try:
            hit_dice_type = int(character.hit_dice.split('d')[1])
            hp_increase = (hit_dice_type // 2) + 1 + character.constitution_mod
            
            # Race-specific HP modifications
            c_race = character.race.lower()
            if 'zwerg' in c_race or 'dwarf' in c_race:
                hp_increase += 1
                
            character.max_hp += hp_increase
            character.current_hp = character.max_hp
        except (ValueError, IndexError):
            pass # fallback if hit_dice is malformed
            
        # Update PB if necessary
        pb = 2
        if character.level >= 17:
            pb = 6
        elif character.level >= 13:
            pb = 5
        elif character.level >= 9:
            pb = 4
        elif character.level >= 5:
            pb = 3
        
        character.save()
        return redirect('character_detail', pk=character.pk)
        
    return render(request, 'characters/character_levelup.html', {'character': character})
