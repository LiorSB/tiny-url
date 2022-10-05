import './Form.css'
import {useState} from "react";
import {getTinyUrl, postCreateTinyUrl} from "../../../../html-request";

export const Form = () => {
    const [name, setName] = useState("");
    const [tinyUrlObj, setTinyUrlObj] = useState({tinyUrl:'',srcUrl:"",creationDate:""});

    const handleSubmit = (event) => {
        event.preventDefault();
        postCreateTinyUrl(name, setTinyUrlObj).then()
    }

    const postFunc = () => {
        getTinyUrl().then()
    }
    return <div className="form-container">
        <span className="form-title-style">Enter a long URL to make a TinyUrl</span>
        <form className="form-style" onSubmit={handleSubmit}>
            <div>
                <label>Enter Original Url: </label>
                <input
                    className="form-input-style"
                    type="text"
                    value={name}
                    onChange={(e) => setName(e.target.value)}
                />
            </div>

            <button type="submit" className="button-submit-form">Make TinyUrl!(post request)</button>
        </form>
        <button className="button-submit-form" onClick={() => postFunc()}>(get request)</button>
        {tinyUrlObj.tinyUrl.length>0 && <div className="tiny-url-container">


           <span>Tiny Url : {tinyUrlObj.tinyUrl}</span>
           <span>Original Url : {tinyUrlObj.srcUrl}</span>
           <span>Creation Time : {tinyUrlObj.creationDate}</span>
        </div>}
    </div>
}
