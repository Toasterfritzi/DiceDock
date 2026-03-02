from django.contrib import admin

from .models import Character


@admin.register(Character)
class CharacterAdmin(admin.ModelAdmin):
    """Admin-Konfiguration für Charaktere."""

    list_display = ('name', 'user', 'level', 'race', 'character_class', 'current_hp', 'max_hp')
    list_filter = ('level', 'character_class', 'race')
    search_fields = ('name', 'user__username', 'race', 'character_class')
    readonly_fields = ('strength_mod', 'dexterity_mod', 'constitution_mod',
                       'intelligence_mod', 'wisdom_mod', 'charisma_mod',
                       'proficiency_bonus')

    fieldsets = (
        ('Grunddaten', {
            'fields': ('user', 'name', 'image', 'character_class', 'subclass',
                       'race', 'background', 'alignment'),
        }),
        ('Attribute', {
            'fields': ('strength', 'dexterity', 'constitution',
                       'intelligence', 'wisdom', 'charisma',
                       'available_stat_points'),
        }),
        ('Modifikatoren (berechnet)', {
            'fields': ('strength_mod', 'dexterity_mod', 'constitution_mod',
                       'intelligence_mod', 'wisdom_mod', 'charisma_mod',
                       'proficiency_bonus'),
            'classes': ('collapse',),
        }),
        ('Kampf & Leben', {
            'fields': ('armor_class', 'speed', 'max_hp', 'current_hp',
                       'temp_hp', 'hit_dice', 'hit_dice_total'),
        }),
        ('Erfahrung', {
            'fields': ('level', 'experience', 'max_experience'),
        }),
        ('Ausrüstung & Währung', {
            'fields': ('equipment', 'gold', 'silver', 'copper',
                       'weapons', 'inventory'),
        }),
        ('Fertigkeiten & Zauber', {
            'fields': ('proficiencies', 'spell_slots'),
        }),
        ('Persönlichkeit', {
            'fields': ('personality_traits', 'ideals', 'bonds', 'flaws',
                       'backstory', 'appearance'),
            'classes': ('collapse',),
        }),
    )
