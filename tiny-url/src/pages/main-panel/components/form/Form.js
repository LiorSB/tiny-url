import './Form.css'
import {useState} from "react";
export const Form=()=>{
    const [name, setName] = useState("");

    const handleSubmit = (event) => {
        event.preventDefault();
        alert(`The name you entered was: ${name}`);
    }

    return <div className="form-container">
        <span className="form-title-style">Enter a long URL to make a TinyUrl</span>
        <form className="form-style" onSubmit={handleSubmit}>
            <div>
                <label>Enter Original Url:  </label>
                <input
                    className="form-input-style"
                    type="text"
                    value={name}
                    onChange={(e) => setName(e.target.value)}
                />
            </div>

          <button type="submit" className="button-submit-form">Make TinyUrl!</button>
        </form>
    </div>
}
