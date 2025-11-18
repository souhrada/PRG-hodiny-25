# datetime je příliš dlouhý název, proto jej importujeme pod zkratkou dt
import datetime as dt

# vytváříme proměnnou cas, pod kterou uložíme momentální čas
cas = dt.datetime.now()


# Různé způsoby přístupu k současnému času

# celý čas
print(cas)

# pouze měsíc, den, rok, second
print(cas.month)
print(cas.day)
print(cas.year)
print(cas.second)

# delta time používáme pro odečítání, přičítání nebo porovnání času


print(f"Teď je {cas}")

minus10 = cas - dt.timedelta(minutes=10)
print(f"Momentální čas -10 minut je {minus10}")

# pomocí delty můžeme vytvořit vlastní, ve formátu:
# roky, měsíce, hodiny, minuty, sekundy, milisekundy
vlastni_cas = dt.datetime(2025, 11, 18, 15, 5)
print(vlastni_cas)

cas_do_prestavky = vlastni_cas - cas
print(f"Do nejbližší oficiální přestávky zbývá {cas_do_prestavky}")

# vem čas, udělej z něj string, rozděl string tam, kde jsou dvoutečky, pak ho spoj, s dvoutečkama, ale spoj
# pouze prvních 7 věcí
# str() vytvoří z něčeho string
# .split rozděluje string na základě nějakého znaku
# .join spojuje do string a ke spojení používá znak
# [:7] znemaná od indexu 0 po index 7
print(":".join(str(cas_do_prestavky).split(":"))[:7])