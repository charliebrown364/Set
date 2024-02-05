import ParentStrat from './parentStrat.js';

class InputStrat {

    constructor() {
        this.simpleBoard = null;
        this.name = 'input';
        this.turn = 0;
        this.playerNum = null;
        this.isManual = true;
    }

    chooseTranslation(translations, shipCoords, plrInput) {
        
        if (!plrInput) return;

        let translation = this.getInputTranslation(plrInput, shipCoords[1]);

        if (translations.find(el => this.sameArray(translation, el)) == undefined) {
            console.log('That doesnt work');
            console.log('gonna do that later');
            return [0, 0];
        }

        return translation;

    }

    chooseTarget(shipInfo, combatOrder, plrInput) {

        let opponentShips = combatOrder.filter(ship => ship.playerNum != shipInfo.playerNum && ship.hp > 0);

        if (opponentShips.length == 1) return opponentShips[0];
        if (!plrInput) return;

        let [targName, targNum] = plrInput.split(' ');
        
        for (let ship of opponentShips) {
            if (ship.name.toLowerCase() == targName.toLowerCase() && ship.shipNum == targNum) {
                return ship;
            }
        }

        console.log(`Opponent does not have ${targName} ${targNum}, try again`);
        console.log('just gonna skip that for now');

        return opponentShips[Math.floor(Math.random() * opponentShips.length)];

    }

}


export default InputStrat;