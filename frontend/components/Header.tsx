import { Box, Link } from '@mui/joy';
import { DesktopNavigation } from './DesktopNavigation';
import { usePageContext } from 'vike-react/usePageContext';
import { constants } from '../data/constants';
import SmallLogo from '../assets/SmallLogo.png';

export const Header = () => {
    const pageContext = usePageContext();

    return (
        <Box
            sx={(theme) => ({
                position: 'fixed',
                width: '100%',
                zIndex: constants.HEADER_Z_INDEX,
                display: 'flex',
                flexDirection: 'row',
                justifyContent: 'space-evenly',
                gap: 2,
                paddingInline: 5,
                background: theme.palette.background.level1,
                boxShadow: theme.shadow.xs,
            })}
        >

            <Link href='/'>
                <Box
                    component='img'
                    src={SmallLogo}
                    alt='Shot Sense'
                    sx={{ height: { xs: '50px', lg: '80px' } }}
                />
            </Link>
            <DesktopNavigation path={pageContext.urlPathname} />
        </Box>
    );
};
