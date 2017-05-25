# OSRS API Wrapper

Allows simple access to Oldschool Runescape's API. Currently supports the only two APIs OSRS has. (Hiscores and GE)

Below are a few examples.

### Hiscores

```python
>>> from const import AccountType
>>> from hiscores import Hiscores
>>> zezima = Hiscores('zezima')
>>> zezima.skills
{'runecrafting': rank-426168 level-24 xp-7103, 'woodcutting': rank-182746     level-73 xp-1002436, ... }
>>> zezima.skills['attack'].level
71
>>> zezima.skills['attack'].xp_tnl()
83344
>>> zezima.max_skill().name
'firemaking'
>>> def very_close_to_level(hiscore, skill):
...     return hiscore.skills[skill].xp_tnl() < 500
>>> zezima.filter(very_close_to_level)
{'construction': rank-355139 level-31 xp-15964}
>>> lynx = Hiscores('Lynx Titan')
>>> mammal = Hiscores('mr mammal')
>>> lynx > mammal
True
>>> iron_mammal = Hiscores('iron mammal', AccountType.IRONMAN)
>>> iron_mammal.rank
1006
```

### Grand Exchange

```python
>>> from grandexchange import GrandExchange
>>> from item import Item
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