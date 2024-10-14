import styles from './App.module.css';
import { CityService } from './components/city_service';
import { Header } from './components/header';


function App() {
    return (
        <div class={styles.App}>
            {/*The header bar*/}
            <Header />

            {/*The VAAS Service with the Globe and Map selection tool -- 100 -> 100% width of the screen*/}
            <CityService vaas_portion="100"/>
        </div>
    );
}

export default App;
