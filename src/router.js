import { isLoggedIn } from './auth'; // Assume this function checks if the user is logged in
import { BrowserRouter as Router, Route, Redirect, Switch } from 'react-router-dom';

function PrivateRoute({ component: Component, ...rest }) {
    return (
        <Route
            {...rest}
            render={(props) =>
                isLoggedIn() ? (
                    <Component {...props} />
                ) : (
                    <Redirect to="/about" />
                )
            }
        />
    );
}

export default function AppRouter() {
    return (
        <Router>
            <Switch>
                {/* ...existing code... */}
                <Route path="/about" component={AboutPage} />
                <Route path="/contact" component={ContactPage} />
                <PrivateRoute path="/second-page" component={SecondPage} />
                {/* ...existing code... */}
            </Switch>
        </Router>
    );
}
