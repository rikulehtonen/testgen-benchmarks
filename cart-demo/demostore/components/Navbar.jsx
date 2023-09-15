import Link from 'next/link';
import { useSelector } from 'react-redux';
import styles from '../styles/Navbar.module.css';

const Navbar = () => {
  const cart = useSelector((state) => state.cart);

  const getItemsCount = () => {
    return "Cart (" + cart.reduce((accumulator, item) => accumulator + item.quantity, 0) + ")"
  };

  return (
    <nav className={styles.navbar}>
      <h6 className={styles.logo}>ROBO_STORE</h6>
      <ul className={styles.links}>
        <li className={styles.navlink}>
          <Link href="/">Home</Link>
        </li>
        <li className={styles.navlink}>
          <Link href="/shop">Shop</Link>
        </li>
        <li className={styles.navlink}>
          <Link href="/cart">
            <a>{getItemsCount()}</a>
          </Link>
        </li>
      </ul>
    </nav>
  );
};

export default Navbar;
