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
    50: '#e8f8ec',
    100: '#d1f1d9',
    200: '#a4e4b2',
    300: '#70d788',
    400: '#4cc85e',
    500: '#2db940',
    600: '#24912e',
    700: '#1a6a21',
    800: '#114216',
    900: '#0c3011',
    solidBg: 'var(--joy-palette-primary-400)',
    solidActiveBg: 'var(--joy-palette-primary-500)',
    outlinedBorder: 'var(--joy-palette-primary-500)',
    outlinedColor: 'var(--joy-palette-primary-700)',
    outlinedActiveBg: 'var(--joy-palette-primary-100)',
    softColor: 'var(--joy-palette-primary-800)',
    softBg: 'var(--joy-palette-primary-200)',
    softActiveBg: 'var(--joy-palette-primary-300)',
    plainColor: 'var(--joy-palette-primary-700)',
    plainActiveBg: 'var(--joy-palette-primary-100)',
};


const secondary = {
    50: '#f6e8ff',
    100: '#e6ccff',
    200: '#c299ff',
    300: '#9966ff',
    400: '#8041ff',
    500: '#6623e0',
    600: '#5017b3',
    700: '#3a0d85',
    800: '#28085c',
    900: '#19063a',
    solidBg: 'var(--joy-palette-secondary-400)',
    solidHoverBg: 'var(--joy-palette-secondary-600)',
    solidActiveBg: 'var(--joy-palette-secondary-500)',
    outlinedBorder: 'var(--joy-palette-secondary-500)',
    outlinedColor: 'var(--joy-palette-secondary-700)',
    outlinedActiveBg: 'var(--joy-palette-secondary-100)',
    softColor: 'var(--joy-palette-secondary-800)',
    softBg: 'var(--joy-palette-secondary-200)',
    softActiveBg: 'var(--joy-palette-secondary-300)',
    plainColor: 'var(--joy-palette-secondary-700)',
    plainActiveBg: 'var(--joy-palette-secondary-100)',
    solidColor: 'white',
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
