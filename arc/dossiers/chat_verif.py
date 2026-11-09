# Vérifications de Qui a mis le chat dans la boîte v0.2 (bibliothèque standard seulement)
import sys, math
out = []
def ok(label, cond):
    out.append(f"{label}   {'OK' if cond else 'ECHEC'}"); assert cond, label
masse, conso, vol, fo2 = 4.0, 4.0, 50.0, 0.209
o2_h = masse * conso * 60 / 1000        # litres par heure
o2_box = vol * fo2
part = o2_h / o2_box * 100
ok(f"Oxygène consommé en une heure : {o2_h:.2f} L ; oxygène de la chambre : {o2_box:.2f} L ; part consommée {part:.1f} %",
   abs(o2_h - 0.96) < 1e-9 and abs(o2_box - 10.45) < 1e-9 and 9 < part < 10)
lam = math.log(2)
ok(f"Activité pour une demi-chance en une heure : ln 2 = {lam:.3f} désintégration par heure", abs(math.exp(-lam) - 0.5) < 1e-12)
ok("Respirations en une heure au rythme de repos (25 par minute) : 1500", 25 * 60 == 1500)
src = open(sys.argv[1], encoding="utf-8").read() if len(sys.argv) > 1 else ""
ok("Typographie : aucun tiret cadratin", "—" not in src)
print("\n".join(out))
