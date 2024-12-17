import axios from "axios";

export function check(): Boolean {
    axios.get("http://127.0.0.1:5000/api/auth/state")
        .then(res => {
            return res.data.logged === "true";
        })
    return false;
}

// export default check()
