import {reactive} from "vue";
import {io} from "socket.io-client";

export const state = reactive({
    connected: false,
    fooEvents: [],
    barEvents: []
});

export const socket = io(
    "ws://localhost:8000",
    {
        path: "/ws/socket.io/",
        transports: ['websocket']
    }
);

socket.on("connect", () => {
    state.connected = true;
});

socket.on("disconnect", () => {
    state.connected = false;
});

socket.on("connect_error", (err) => {
    console.log(`connect_error due to ${err}`);
});
