import {reactive} from 'vue'
import {getCookie} from "@/utils/cookies";


interface IServer {
    url: String
}

export interface IPlayer {
    uid: String;
    mark: String;
}

interface IStore {
    server: IServer;
    player: IPlayer;
    turn: string,
    board: Array<string>;
    winner: string;
}


// @ts-ignore
export const store: IStore = reactive({
    server: {
        url: "localhost:8000"
    },
    player: {
        uid: getCookie("ttt_uid"),
        mark: ""
    },
    board: ["", "", "", "", "", "", "", "", ""],
    turn: "",
    winner: "",
})
