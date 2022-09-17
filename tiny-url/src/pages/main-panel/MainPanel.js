import {Header} from "./components/header/Header";
import {Form} from "./components/form/Form";
import './MainPanel.css'
export const MainPanel = () => {
    return <div className="main-panel-container">
        <Header/>
        <Form/>
    </div>
}
