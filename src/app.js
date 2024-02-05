import express from 'express';
import http from 'http';
import { Server } from 'socket.io';

import Game from './game.js';
import InputStrat from './inputStrat.js';

const app = express();
const httpServer = http.Server(app);
const io = new Server(httpServer);

app.use(express.static('client'));
app.get('/', (_, res) => res.sendFile(`${__dirname}/client/index.html`));

let game = null;
let clientSockets = {}; 

io.on('connection', (socket) => {

    let socketId = socket.id;
    clientSockets[socketId] = socket;

    console.log(`Client socket connected: ${socket.id}`);

    socket.on('disconnect', () => {
        console.log(`Client socket disconnected: ${socketId}`);
        delete clientSockets[socketId];
    });

    socket.emit('initialize UI');

    /* EDIT THIS */

    socket.on('initialize game', () => {
        game = new Game(clientSockets);
        game.initializeGame();
        game.display();
    });

    socket.on('next turn', () => {
        if (game) game.run();
    });

    socket.on('submit input', (input) => {
        console.log(`new input: ${input}`);
        if (game) game.playerInput = input;
    });

});

let port = 3000;
httpServer.listen(port, () => console.log(`Listening on *:${port}`));