import { City } from './city';
import { createSignal } from 'solid-js';

export const [serviceType, setServiceType] = createSignal('park');

export function Header() {
    return <>
        <City />
    </>
}
