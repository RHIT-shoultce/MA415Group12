import type { PaletteRange } from '@mui/joy/styles';

declare module 'hono' {
  interface ContextVariableMap {
    user?: null | UserRecord;
  }
}

declare module '@mui/joy/styles' {
  interface ColorPalettePropOverrides {
    secondary: true;
  }

  interface Palette {
    primary: {
      150: string;
      175: string;
      350: string;
      650: string;
    } & PaletteRange;
    secondary: { 350: string } & PaletteRange;
  }

  interface Breakpoints {
    values: {
      bigMobile: number;
      lg: number;
      md: number;
      sm: number;
      smallMobile: number;
      xl: number;
      xs: number;
      xxs: number;
    };
  }
  interface BreakpointOverrides {
    bigMobile: true;
    smallMobile: true;
    xxs: true;
  }
}
