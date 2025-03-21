import { Box, Typography, useTheme } from '@mui/joy';
import { FaBasketball } from 'react-icons/fa6';
import '../layouts/style.css';

interface FullScreenLoaderProps {
    label?: string;
}

export const FullScreenLoader = ({ label }: FullScreenLoaderProps) => {
    const theme = useTheme();

    return (
        <Box
            sx={{
                alignItems: 'center',
                display: 'flex',
                flex: 1,
                flexDirection: 'column',
                gap: 2,
                height: '100px',
                justifyContent: 'center',
                position: 'relative',
            }}
        >
            <FaBasketball
                className='spinning-basketball'
                color={theme.palette.secondary.solidBg}
            />
            <Typography>{label ?? 'Loading...'}</Typography>
        </Box>
    );
};
