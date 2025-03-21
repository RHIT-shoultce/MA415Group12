import { Box } from '@mui/joy';
import { navigationLinks } from '../data/navigationLinks';
import { NavLink } from './NavLink';

interface DesktopNavigationProps {
    path: string;
}

export const DesktopNavigation = (props: DesktopNavigationProps) => {

    return (
        <>
            <Box sx={{
                display: { xs: 'none', lg: 'flex' },
                alignItems: 'left',
                width: '100%',
                justifyContent: 'spaced-evenly',
            }}>
                {navigationLinks
                    .map((page) => (
                        <NavLink
                            active={page.href === props.path}
                            href={page.href}
                            key={page.label}
                            label={page.label}
                        />
                    ))}
            </Box>
        </>
    );
};
