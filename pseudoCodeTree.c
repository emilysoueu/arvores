function exp: árvoreSintática;
var temp, novaTemp,: árvoreSintática;

beguin
	temp := termo;
	while marca = + ou marca - do 
		case marca of:
		+ : casamento (+);
		    novaTemp := criaNóOp(+);
		    filhoEsquerdo(novaTemp) := temp;
		    filhoDireito(novaTemp) := termo;
		    temp := novaTemp;
		- : casamento (-);
		    novaTemp := criaNóOp(-);
		    filhoEsquerdo(novaTemp) := temp;
		    filhoDireito(novaTemp):= termo;
		    temp := novaTemp;
		end case;
	end while;
	return temp;
end exp; 
