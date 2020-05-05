# OSRS API Wrapper

Allows simple access to Oldschool Runescape's API. Currently supports the only two APIs OSRS has. (Hiscores and GE)

### Install

```
pip install python-osrsapi
```

### Dev Install

```
make dev
```

### Hiscores

```python
>>> from osrs_api.const import AccountType
>>> from osrs_api import Hiscores
>>> zezima = Hiscores('zezima')
>>> zezima.skills
{'attack': Skill(name=attack, rank=614026, level=76, xp=1343681), 'defence': ...}
>>> zezima.skills['attack'].level
76
>>> zezima.skills['attack'].xp_tnl()
131900
>>> zezima.max_skill().name
'firemaking'
>>> def maxed_skills(hiscore, skill):
...     return hiscore.skills[skill].level == 99
>>> zezima.filter(maxed_skills)
{'firemaking': Skill(name=firemaking, rank=108780, level=99, xp=13034646)}
>>> lynx = Hiscores('Lynx Titan')
>>> mammal = Hiscores('mr mammal')
>>> lynx > mammal
True
>>> iron_mammal = Hiscores('iron mammal', AccountType.IRONMAN)
>>> iron_mammal.rank
1052
```

### Grand Exchange

```python
>>> from osrs_api import GrandExchange
>>> from osrs_api import Item
>>> whip_id = Item.get_ids('abyssal whip')
>>> whip_id
4151
>>> whip = GrandExchange.item(whip_id)
>>> whip.description
'A weapon from the abyss.'
>>> whip.price(), whip.is_mem
(1648785, True)
>>> thirty_days = whip.price_info.trend_30
>>> thirty_days.trend, thirty_days.change
('negative', -18.0)
>>> dagger_ids = Item.get_ids('rune dag')
# If you enter a partial name, you will get a list of all possible matches.
>>> dagger_ids
[5696, 5678, 1229, 1213]
# Names
>>> [Item.id_to_name(id) for id in dagger_ids]
['Rune dagger(p++)', 'Rune dagger(p+)', 'Rune dagger(p)', 'Rune dagger']
>>> GrandExchange.item(dagger_ids[0]).description
'The blade is covered with a nasty poison.'
```