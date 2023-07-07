import {reactive} from 'vue'
import {getCookie} from "@/utils/cookies";


interface IServer {
    url: String
}

export interface IPlayer {
    uid: String;
    mark: String;
}


// @ts-ignore
export const store: { server: IServer, player: IPlayer, board: Array<string>, winner: string } = reactive({
    server: {
        url: "localhost:8000"
    },
    player: {
        uid: getCookie("ttt_uid"),
        mark: ""
    },
    board: ["", "", "", "", "", "", "", "", ""],
    winner: ""
})