import { FullScreenLoader } from '../components/FullScreenLoader';
import { Interpolation } from '@emotion/react';
import {
    CssBaseline,
    CssVarsProvider,
    CssVarsThemeOptions,
    extendTheme,
    GlobalStyles,
    Theme,
} from '@mui/joy';
import { type ReactNode, useEffect, useState } from 'react';
import '../layouts/style.css';

const primary = {
    50: '#f2faff',
    100: '#f2faff',
    150: '#9795b5',
    175: 'rgba(96, 130, 182, 0.6)',
    200: '#ace4ff',
    300: '#00b2ff',
    350: 'rgba(0, 141, 228, 0.15)',
    400: '#008de4',
    500: '#0070c4',
    600: '#0055a5',
    650: 'rgba(0, 50, 98, 0.15)',
    700: '#003c86',
    800: '#002469',
    900: '#001a5b',
    outlinedActiveBg: 'var(--joy-palette-primary-100)',
    outlinedBorder: 'var(--joy-palette-primary-500)',
    outlinedColor: 'var(--joy-palette-primary-700)',
    plainActiveBg: 'var(--joy-palette-primary-100)',
    plainColor: 'var(--joy-palette-primary-700)',
    softActiveBg: 'var(--joy-palette-primary-300)',
    softBg: 'var(--joy-palette-primary-350)',
    softColor: 'var(--joy-palette-primary-800)',
    solidActiveBg: 'var(--joy-palette-primary-500)',
    solidBg: 'var(--joy-palette-primary-400)',
};

const secondary = {
    50: '#fff5ec',
    75: '#e0e0ff',
    90: '#f5f5f5',
    100: '#dfe0df',
    200: '#bca79d',
    300: '#c57000',
    350: 'rgba(228, 87, 0, 0.15)',
    400: '#e45700',
    500: '#c03800',
    600: '#9b1100',
    700: '#9e1500',
    800: '#7d0000',
    900: '#5f0000',
    outlinedActiveBg: 'var(--joy-palette-secondary-100)',
    outlinedBorder: 'var(--joy-palette-secondary-500)',
    outlinedColor: 'var(--joy-palette-secondary-700)',
    plainActiveBg: 'var(--joy-palette-secondary-100)',
    plainColor: 'var(--joy-palette-secondary-700)',
    softActiveBg: 'var(--joy-palette-secondary-300)',
    softBg: 'var(--joy-palette-secondary-350)',
    softColor: 'var(--joy-palette-secondary-800)',
    solidActiveBg: 'var(--joy-palette-secondary-500)',
    solidBg: 'var(--joy-palette-secondary-400)',
    solidColor: 'white',
    solidHoverBg: 'var(--joy-palette-secondary-600)',
};

const theme = extendTheme({
    breakpoints: {
        values: {
            bigMobile: 380,
            lg: 992,
            md: 768,
            sm: 620,
            smallMobile: 330,
            xl: 1200,
            xs: 500,
            xxs: 0,
        },
    },
    colorSchemes: {
        dark: {
            palette: {
                primary,
                secondary,
            },
        },
        light: {
            palette: {
                primary,
                secondary,
            },
        },
    },
    fontFamily: {
        body: 'DM Sans',
        display: 'DM Sans',
    },
    radius: {
        lg: '30px',
        md: '24px',
        sm: '20px',
        xl: '35px',
        xs: '12px',
    },
} as CssVarsThemeOptions);

const iconConfig: Interpolation<Theme> = {
    '.ui-icon svg': {
        color: 'var(--Icon-color)',
        fontSize: 'var(--Icon-fontSize, 20px)',
        height: '1em',
        margin: 'var(--Icon-margin)',
        width: '1em',
    },
};

export const JoyLayout = ({ children }: { children: ReactNode }) => {
    const [mounted, setMounted] = useState(false);

    useEffect(() => setMounted(true), []);

    return (
        <CssVarsProvider
            defaultMode='light'
            disableNestedContext={true}
            theme={theme}
        >
            <CssBaseline />
            <GlobalStyles styles={iconConfig} />
            {mounted ? children : <FullScreenLoader label="Retrieving cool stats..." />}
        </CssVarsProvider>
    );
};
